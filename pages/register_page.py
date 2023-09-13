from playwright.sync_api import Page
import config
import pages


class RegisterPage:

    def open_index_page(self, page) -> None:
        pages.base_page.open_page(config.url.DOMIAN, page)