import allure
import config
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
 
    def open_register_page(self, page) -> None:
        components.header_links.open_register_page_header_menu(page)

    def filling_registration_form(self, page):
        with allure.step('Ставим флаг в чекбоксе Gender'):
            pages.base_page.check_the_checkbox(page, self._GENDER_CHECKBOX_LOCATOR)
        with allure.step('Заполняем поля формы регистрации.'):
            pages.base_page.fill_the_field_by_label(page, 'First name', self.fake_firstrname)
            pages.base_page.fill_the_field_by_label(page, 'Last name', self.fake_lastname)
            pages.base_page.fill_the_field_by_label(page, 'Email', self.fake_email)
            pages.base_page.fill_the_field(page, '#Password', 'Ilya_koz12345')
            pages.base_page.fill_the_field(page, '#ConfirmPassword', 'Ilya_koz12345')
            print(self.password_data)
        # with allure.step('Нажимаем на кнопку Register'):
        #     pages.base_page.click(page, '#register-button')





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