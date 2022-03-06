from playwright.sync_api import sync_playwright


with sync_playwright()  as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://speedtest.net')
    page.locator(".start-button:visible").click()
    page.locator("html body.standard-layout.language-en div#container div.pre-fold.mobile-test-complete div.main-content div.main div.container div.pure-g div.pure-u-custom-speedtest div.speedtest-container.main-row div.main-view div div.result-area.result-area-test div div.result-container.clearfix div.result-container-speed.result-container-speed-active div.result-container-data div.result-item-container.result-item-container-align-center div.result-item.result-item-first-class.result-item-download.updated").wait_for(timeout=0)
    page.screenshot(path="screenshot.png")

    