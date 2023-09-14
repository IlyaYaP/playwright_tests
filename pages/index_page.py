import config
import pages
import allure


class IndexPage:

    def open_index_page(self, page) -> None:
        with allure.step('Открываем главную страницу.'):
            pages.base_page.open_page(config.url.DOMIAN, page)