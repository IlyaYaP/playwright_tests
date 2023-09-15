from playwright.sync_api import Page
import allure


class HeaderLinks:

    def open_register_page_header_menu(self, page: Page) -> None:
        with allure.step('Открываем страницу регистрации, нажимая на кнопку Register header.'):
            page.locator("//a[contains(text(), 'Register')]").click()


class TopMenu:

    def open_books(self, page: Page) -> None:
        with allure.step('Открываем вкладку Books в меню header.'):
            page.locator("//ul[@class='top-menu']//a[contains(text(), 'Books')]").click()