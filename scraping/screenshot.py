from playwright.sync_api import sync_playwright

def capture_screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.screenshot(path="chapter_1_screenshot.png", full_page=True)
        browser.close()

    print("📸 Screenshot saved to 'chapter_1_screenshot.png'")
