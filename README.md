# chatgpt_utils
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ChatGPT Utilities to make life more fun

What this does:
Extends ChatGPT for greater customization in the event of a chat window closure.
It simply saves your posts when your local memory is full.  
Why:
This leads to more customized/personalized/focused responses based on what you have already
fed the AI.

This utility requires you interact with the AI.  
You need to create a 'tag' for the AI responses that you would like to 'save'.

**Glossary (Because I make things up)**
-------------------------------------------------------------
ATOTW: At the time of this writing
MEM: How I tag my responses to be 'saved' (written to a local flat file) that I can then 'load' back into a new 
ChatGPT thread manually to 'restore' beyond the base memory.
![img.png](img.png)

**System Build**

Divers:
Chrome
https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json
https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.53/win64/chromedriver-win64.zip

![img_2.png](img_2.png)


Create a Project 

mkdir my_python_app
cd my_python_app
python3 -**m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
touch app.py  # On Windows: type nul > app.py

pip install selenium
pip install playwright
playwright install

pip freeze > requirements.txt

chmod +x app.py


