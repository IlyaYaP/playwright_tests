import allure
import config
import pages
import components


class RegisterPage:

    _GENDER_CHECKBOX_LOCATOR = "#gender-female"

    def open_index_page(self, page) -> None:
        pages.base_page.open_page(config.url.DOMIAN, page)
    
    def open_register_page(self, page) -> None:
        components.header_links.open_register_page(page)

    def filling_registration_form(self, page):
        pages.base_page.check_the_checkbox(page, self._GENDER_CHECKBOX_LOCATOR)
        pages.base_page.fill_the_field(page, 'First name', 'Ilya')
        pages.base_page.fill_the_field(page, 'Last name', 'Kozyrev')
        pages.base_page.fill_the_field(page, 'Email', 'IlKoz@gmail.com')