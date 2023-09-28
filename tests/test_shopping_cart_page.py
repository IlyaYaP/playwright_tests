import pages
import pytest
import time


class TestShoppingCartPage:

    @pytest.mark.shopping_cart_test()
    def test_shopping_cart(self, page, category_locator):
        pages.index_page.open_index_page(page)
        pages.shopping_cart_page.open_categories(page, category_locator)
        time.sleep(5)