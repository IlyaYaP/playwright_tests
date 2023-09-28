import pages
import components
import pytest
import time


class TestShoppingCartPage:

    _CATEGORY_DESKTOP_LOCATOR = "h2 a[title='Show products in category Desktops']"
    
    @pytest.mark.shopping_cart_test()
    def test_shopping_cart(self, page):
        pages.index_page.open_index_page(page)
        components.top_menu.open_computers(page)
        pages.shopping_cart_page.open_categories(page, self._CATEGORY_DESKTOP_LOCATOR)
        time.sleep(5)