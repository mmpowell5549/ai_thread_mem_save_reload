# MIT License
#
# Copyright (c) 2024 Your Name (or GitHub Username)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set Chrome options (Disables SSL verification as a temporary fix)
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevents bot detection

# Set the path to your Chromedriver
service = Service("/WebDrivers/chromedriver.exe")  # Update this path - it is needed
driver = webdriver.Chrome(service=service, options=chrome_options)
#
driver.get("https://x.com/i/grok?conversation=<you put ur id in here>")
# driver.get("https://chatgpt.com/auth/login")

# time.sleep() halts the entire Python process, including interactions with the browser.
# ChromeDriver continues to execute page scripts (JavaScript, animations, etc.) during this time.
# No Selenium commands are executed during the sleep.
# TODO: WebDriverWait(driver, 180).until(
#     lambda driver: driver.execute_script("return document.readyState") == "complete"
# )
time.sleep(60)
# Manual Step - You go out there and log in and navigate to ur page man
# ----------------------------------------------------------------------------
# Wait to ensure page loads (optional, prevents timing issues - if you don't get
# lines 42/48 combined correctly you won't
# be reading the entire chat thread.  The page cache has to load ;))
driver.implicitly_wait(5)

# Find all messages (modify class name based on actual chat structure)
hal_messages = [elem.get_attribute("textContent") for elem in driver.find_elements(By.XPATH, "//*[contains(text(), 'MEM')]") if "MEM" in elem.get_attribute("textContent")]

# Save filtered messages to a file
with open("scan_messages.txt", "w", encoding="utf-8") as f:
    f.write('Start Over\n')
    print('start write')
    for msg in hal_messages:
        print('-----------writing----------')
        f.write(msg + "\n")
        print(msg)

print('Message search loop complete')
# Close the browser
driver.quit()
