import pages
import pytest


class TestRegisterPage:

    @pytest.mark.register_page_test()
    def test_register_page(self, page):
        pages.index_page.open_index_page(page)
        pages.register_page.open_register_page(page)
        pages.register_page.filling_registration_form(page)
        pages.register_page.should_be_successful_register_text(page)
