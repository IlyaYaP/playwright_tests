import allure
import pages
import components
from faker import Faker


class LogInPage:

    def open_log_in_page(self, page):
        components.header_links.open_log_in_page_header_menu(page)

    def filling_log_in_form(self, page):
        with allure.step('Заполняем поля формы входа в учетную запись.'):
            pages.base_page.fill_the_field_by_label(page,
                                                    'Email',
                                                    'IlKoz@gmail.com')
            pages.base_page.fill_the_field_by_label(page,
                                                    'Password',
                                                    'Ilya_koz12345')
        with allure.step('Ставим флаг в чекбоксе RememberMe'):
            pages.base_page.check_the_checkbox(page, '#RememberMe')
        with allure.step('Нажимаем на кнопку Log in'):
            pages.base_page.click(page, '.login-button')

    def should_be_successful_login_text(self, page):
        with allure.step('Проверяем, что мы успешно вошли в учетную запись.'):
            pages.base_page.expect_to_contain_text(page,
                                                   'div.header-links .account',
                                                   'IlKoz@gmail.com')
