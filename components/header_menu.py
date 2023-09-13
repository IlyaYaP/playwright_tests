from playwright.sync_api import Page


class TopMenu:

    def open_books(self, page: Page) -> None:
        page.locator("//ul[@class='top-menu']//a[contains(text(), 'Books')]").click()