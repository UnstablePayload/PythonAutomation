from tkinter import Image
from playwright.sync_api import sync_playwright
import os
from PIL import Image


# Clears the Command Prompt.
def clearscreen():
    os.system("cls")

# Main Program
clearscreen()
with sync_playwright()  as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print('[x] Navigating to Speedtest.net')
    print('[ ] Waiting for speedtest.net to fully load.')
    print('[ ] Running speed test...')
    page.goto('https://speedtest.net')
    clearscreen()
    print('[x] Navigating to Speedtest.net')
    print('[x] Waiting for speedtest.net to fully load.')
    print('[ ] Running speed test...')
    page.locator(".start-button:visible").click()
    clearscreen()
    print('[x] Navigating to Speedtest.net')
    print('[x] Waiting for speedtest.net to fully load.')
    print('[x] Running speed test...')
    page.locator("html body.standard-layout.language-en div#container div.pre-fold.mobile-test-complete div.main-content div.main div.container div.pure-g div.pure-u-custom-speedtest div.speedtest-container.main-row div.main-view div div.result-area.result-area-test div div.result-container.clearfix div.result-container-speed.result-container-speed-active div.result-container-data div.result-item-container.result-item-container-align-center div.result-item.result-item-first-class.result-item-download.updated").wait_for(timeout=0)
    page.screenshot(path="screenshot.png")
    clearscreen()
    print('[x] Navigating to Speedtest.net')
    print('[x] Waiting for speedtest.net to fully load.')
    print('[x] Running speed test...')
    print('Opening Screenshot')
    
img = Image.open('screenshot.png')
img.show()


    
    