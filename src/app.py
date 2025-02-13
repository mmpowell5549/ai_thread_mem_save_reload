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

# Set Chrome options (Disables SSL verification as a temporary fix)
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevents bot detection
chrome_options.add_argument("--user-data-dir=C:\\Users\\YourUsername\\AppData\\Local\\Google\\Chrome\\User Data")  # Windows path
chrome_options.add_argument("--profile-directory=Default")  # Use your existing Chrome profile


# Set the path to your Chromedriver
service = Service("C:\\WebDrivers\\chromedriver.exe")  # Update this path if needed
driver = webdriver.Chrome(service=service, options=chrome_options)

# !/usr/bin/env python3
print("This script can run as an executable!")

# Open the OpenAI chat page
driver.get("https://chatgpt.com/c/<your chat id>")

# Wait to ensure page loads (optional, prevents timing issues)
driver.implicitly_wait(5)

# Find all messages (modify class name based on actual chat structure)
messages = driver.find_elements(By.CLASS_NAME, "message")  # Update class if necessary

# Filter messages that contain "Hal"
hal_messages = [msg.text for msg in messages if "Hal" in msg.text]

# Save filtered messages to a file
with open("scan_messages.txt", "w", encoding="utf-8") as f:
    for msg in hal_messages:
        f.write(msg + "\n")

# Close the browser
driver.quit()
