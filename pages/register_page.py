import allure
import config
import pages
import components


class RegisterPage:

    def open_index_page(self, page) -> None:
        pages.base_page.open_page(config.url.DOMIAN, page)
    
    def open_register_page(self, page) -> None:
        components.header_links.open_register_page(page)