from playwright.sync_api import Page


class BasePage:

    def open_page(self, url, page: Page) -> None:
        page.goto(url)