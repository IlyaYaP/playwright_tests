from playwright.sync_api import Page


class BasePage:

    def open_page(self, url, page: Page) -> None:
        page.goto(url)

    def check_the_checkbox(self, page: Page, locator) -> None:
        page.locator(locator).check()

    def fill_the_field(self, page: Page, label, input_value) -> None:
        page.get_by_label(label).fill(input_value)
