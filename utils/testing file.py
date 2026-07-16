import json
import time

import playwright
from playwright.sync_api import sync_playwright
from pathlib import Path

file_name = Path(__file__).parent.parent/"testdata"/"credentials.json"

with open(file_name,"r") as file:
    data = json.load(file)
    print(data["userCredentials"][0]["userEmail"])
    print(data)

# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False)
# context_new = browser.new_context()
# page = context_new.new_page()
# page.goto("https://rahulshettyacademy.com/client/")
# page.get_by_placeholder("email@example.com").fill("shashikanth10@gmail.com")
# time.sleep(5)
