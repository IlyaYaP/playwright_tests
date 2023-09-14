from playwright.sync_api import Page
import allure


class HeaderLinks:

    def open_register_page(self, page: Page) -> None:
        with allure.step('Открываем страницу регистрации.'):
            page.locator("//a[contains(text(), 'Register')]").click()


class TopMenu:

    def open_books(self, page: Page) -> None:
        with allure.step('Открываем вкладку Books в меню header.'):
            page.locator("//ul[@class='top-menu']//a[contains(text(), 'Books')]").click()