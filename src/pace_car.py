import asyncio

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

from data.classes import Cherry
from data.classes.TrackBuilder import TrackBuilder

chrome_runtime_script = """
(() => {
 // Inject chrome.runtime if missing or incomplete
 if (!window.chrome) {
 // @ts-ignore
 window.chrome = {};
 }
 if (!window.chrome.runtime) {
 // @ts-ignore
 window.chrome.runtime = {};
 }

 const runtime = window.chrome.runtime;

 // Basic properties and methods to mimic real Chrome
 runtime.onConnect = {
 addListener: () => {},
 removeListener: () => {},
 hasListener: () => false
 };
 runtime.onMessage = {
 addListener: () => {},
 removeListener: () => {},
 hasListener: () => false
 };
 runtime.sendMessage = () => {};
 runtime.connect = () => ({
 postMessage: () => {},
 onMessage: { addListener: () => {} },
 disconnect: () => {}
 });

 // Fake some common properties
 Object.defineProperty(runtime, 'id', { get: () => 'playwright-fake-extension-id' });
 Object.defineProperty(runtime, 'lastError', { get: () => undefined });
})();
"""

# 2. Permissions API fix (force standard states instead of "default")
permissions_script = """
(() => {
 const originalQuery = Permission.prototype.query;
 Permission.prototype.query = function() {
 return Promise.resolve({
 state: this.name === 'notifications' ? 'granted' : 'prompt' // Or 'denied' as needed
 });
 };
})();
"""

# 4. Additional common evasions (optional but helpful)
extra_evasions = """
// Remove automation indicators
delete navigator.__proto__.webdriver;

// Spoof languages if not using Stealth's override
Object.defineProperty(navigator, 'languages', {
 get: () => ['en-US', 'en']
});
"""

# Run this FIRST before any page scripts or navigations.
WEBDRIVER_FIX_SCRIPT = """
        const originalQuery = window.navigator.permissions.query;
        window.navigator.permissions.query = (parameters) => (
          parameters.name === 'notifications'
            ? Promise.resolve({ state: Notification.permission })
            : originalQuery(parameters)
        );
"""


async def build_browser(p):
    browser = await p.chromium.launch(
        headless=False,
        channel="chrome",
        args=[
            "--disable-blink-features=AutomationControlled",
        ]
    )

    user_agent_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"

    context = await browser.new_context(
        user_agent=user_agent_string,
        locale="en-US",
        viewport={"width": 1000, "height": 800},
        extra_http_headers={
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="143", "Chromium";v="143"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'accept-language': 'en-US,en;q=0.9',
            'x-playwright-user-agent': None
        }
    )

    custom_languages = ("en-US", "en")
    stealth = Stealth(
        navigator_languages_override=custom_languages,
        init_scripts_only=True,
        navigator_webdriver=True,
        navigator_permissions=False,
        navigator_plugins=True
    )

    await stealth.apply_stealth_async(context)

    await context.add_init_script(script=chrome_runtime_script)
    await context.add_init_script(script=WEBDRIVER_FIX_SCRIPT)
    # DO not use this one
    # await context.add_init_script(script=webdriver_script)
    # await context.add_init_script(script=extra_evasions)

    page = await context.new_page()

    return page, context, browser


async def manual_crawl():
    async with Stealth().use_async(async_playwright()) as p:

        page, context, browser = await build_browser(p)

        try:
            while True:
                url = await asyncio.get_event_loop().run_in_executor(
                    None, input, "URL > "
                )

                url = url.strip()

                # Exit command
                if url.lower() in {"q", "quit", "exit"}:
                    print("Shutting down... goodbye!")
                    break

                # Skip empty input
                if not url:
                    print("URL cannot be empty, try again.\n")
                    continue

                if not (url.startswith("http://") or url.startswith("https://")):
                    url = "https://" + url
                    print(f"→ Using: {url}")

                try:
                    print(f"Navigating to {url} ...")
                    response = await page.goto(url, wait_until="domcontentloaded", timeout=30_000)

                    title = await page.title()
                    status = response.status if response else "Unknown"

                    print(f"Success! Title: {title}")
                    print(f"Status code: {status}\n")

                except Exception as e:
                    print(f"Failed to load page: {e}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nInterrupted by user, exiting...")
        finally:
            # Always clean up
            await context.close()
            await browser.close()


async def crawl_track(queue: asyncio.Queue):
    domcontentloaded_event = asyncio.Event()
    async with Stealth().use_async(async_playwright()) as p:
        try:
            while True:

                cherry = await queue.get()

                if cherry is None:
                    break

                page, context, browser = await build_browser(p)
                try:
                    captured_responses = []

                    async def handle_response(response):
                        # Only capture the main document response (not assets like images/js)
                        nonlocal captured_responses
                        if response.request.resource_type == "document":
                            captured_responses.append(response)
                            print(f"Captured main response: {response.url} -> {response.status}")

                    async def on_domcontentloaded():
                        cherry.html = await page.content()  # This gets the current rendered HTML
                        if cherry.html:
                            cherry.soup = BeautifulSoup(cherry.html, "html.parser")
                            cherry.pick()
                        domcontentloaded_event.set()  # Signal that the event occurred

                    page.on("response", handle_response)
                    page.on("domcontentloaded", on_domcontentloaded)

                    response = await page.goto(cherry.url, wait_until="domcontentloaded", timeout=60_000)
                    status = response.status if response else "Unknown"
                    print(f"Status code: {status}\n")

                    # await domcontentloaded_event.wait()
                    try:
                        await asyncio.wait_for(domcontentloaded_event.wait(), timeout=30.0)  # Wait up to 10 seconds
                        print("DOMContentLoaded event received within timeout")
                    except asyncio.TimeoutError:
                        print("Timed out waiting for DOMContentLoaded event")

                    queue.task_done()

                    await browser.close()

                except Exception as e:
                    print(f"Failed to load page: {e}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nInterrupted by user, exiting...")
        finally:
            # Always clean up
            await context.close()
            await browser.close()


async def get_track():
    race_track = TrackBuilder()
    race_track.BuildLineUp()

    queue = asyncio.Queue()

    for cherry in race_track.track:
        await queue.put(cherry)

    num_workers = 1

    workers = [asyncio.create_task(crawl_track(queue)) for _ in range(num_workers)]

    await queue.join()

    # Send sentinel values (None) to stop all workers
    for _ in range(num_workers):
        await queue.put(None)

    await asyncio.gather(*workers)

    print("All items processed and workers shut down.", flush=True)


if __name__ == "__main__":
    asyncio.run(get_track())
