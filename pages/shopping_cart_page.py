import allure
import pages
import components


class ShoppingCartPage:

    # _CATEGORY_DESKTOP_LOCATOR = "h2 a[title='Show products in category Desktops']"

    def open_categories(self, page, category_locator) -> None:
        pages.base_page.click(page, category_locator)
