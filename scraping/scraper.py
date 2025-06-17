from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def fetch_chapter_text(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")
        content = page.content()
        browser.close()

    soup = BeautifulSoup(content, "html.parser")
    text = soup.find("div", {"class": "mw-parser-output"})
    paragraphs = text.find_all("p")
    chapter_text = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

    with open("chapter_1_raw.txt", "w", encoding="utf-8") as f:
        f.write(chapter_text)

    print("✅ Chapter text saved to 'chapter_1_raw.txt'")
    return chapter_text
