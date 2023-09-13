from playwright.sync_api import Page
import config
import pages
import components


class RegisterPage:

    def open_index_page(self, page) -> None:
        pages.base_page.open_page(config.url.DOMIAN, page)
    
    def open_register_page(self, page) -> None:
        components.top_menu.open_books(page) 