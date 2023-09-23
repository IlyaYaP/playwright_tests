import allure
import pages
import components
from faker import Faker


class RegisterPage:

    fake = Faker()
    fake_firstrname = fake.first_name()
    fake_lastname = fake.last_name()
    fake_email = fake.email()

    password_data = []
    fake_password = [fake.password()]
    password_data.extend(fake_password)

    _GENDER_CHECKBOX_LOCATOR = "#gender-female"
    _PASSWORD_FIELD_LOCATOR = '#Password'
    _CONF_PASSWORD_LOCATOR = '#ConfirmPassword'
    _REGISTER_BUTTON_LOCATOR = '#register-button'
    _REGISTER_TEXT_LOCATOR = 'div.result'

    def open_register_page(self, page) -> None:
        components.header_links.open_register_page_header_menu(page)

    def filling_registration_form(self, page):
        with allure.step('Ставим флаг в чекбоксе Gender'):
            pages.base_page.check_the_checkbox(page,
                                               self._GENDER_CHECKBOX_LOCATOR)
        with allure.step('Заполняем поля формы регистрации.'):
            pages.base_page.fill_the_field_by_label(page,
                                                    'First name',
                                                    self.fake_firstrname)
            pages.base_page.fill_the_field_by_label(page,
                                                    'Last name',
                                                    self.fake_lastname)
            pages.base_page.fill_the_field_by_label(page,
                                                    'Email',
                                                    self.fake_email)
            pages.base_page.fill_the_field(page,
                                           self._PASSWORD_FIELD_LOCATOR,
                                           self.password_data[0])
            pages.base_page.fill_the_field(page,
                                           self._CONF_PASSWORD_LOCATOR,
                                           self.password_data[0])
        with allure.step('Нажимаем на кнопку Register'):
            pages.base_page.click(page, self._REGISTER_BUTTON_LOCATOR)

    def should_be_successful_register_text(self, page):
        with allure.step('Проверяем, что регистрация прошла успешно.'):
            pages.base_page.expect_to_contain_text(page,
                                                   self._REGISTER_TEXT_LOCATOR,
                                                   'Your registration completed')




    # _GENDER_CHECKBOX_LOCATOR = "#gender-female"
 
    # def open_register_page(self, page) -> None:
    #     components.header_links.open_register_page_header_menu(page)

    # def filling_registration_form(self, page):
    #     with allure.step('Ставим флаг в чекбоксе Gender'):
    #         pages.base_page.check_the_checkbox(page, self._GENDER_CHECKBOX_LOCATOR)
    #     with allure.step('Заполняем поля формы регистрации.'):
    #         pages.base_page.fill_the_field_by_label(page, 'First name', 'Ilya')
    #         pages.base_page.fill_the_field_by_label(page, 'Last name', 'Kozyrev')
    #         pages.base_page.fill_the_field_by_label(page, 'Email', 'IlKoz@gmail.com')
    #         pages.base_page.fill_the_field(page, '#Password', 'Ilya_koz12345')
    #         pages.base_page.fill_the_field(page, '#ConfirmPassword', 'Ilya_koz12345')
    #     with allure.step('Нажимаем на кнопку Register'):
    #         pages.base_page.click(page, '#register-button')