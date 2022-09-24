
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def title_filter(title):
    string1 = "\/:*?\"<>|"
    for s1 in string1:
        title = title.replace(s1," ")
    return title

def downloader(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()
    for page_node in range(1,206):
        for node in range(1,31):
            try:
                page.goto(f"https://xz.aliyun.com/?page={page_node}")
                time.sleep(3)
                selector =f'// *[ @ id = "includeList"] / table / tbody / tr[{node}] / td / p[1] / a'
                page.locator(selector).click()
                time.sleep(25)
                title = page.title()
                title = title_filter(title)
                page.pdf(path=f"newkonwer/{page_node}/{title}.pdf")
                print(page_node,node,title)
            except Exception as e:
                print(e)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    downloader(playwright)