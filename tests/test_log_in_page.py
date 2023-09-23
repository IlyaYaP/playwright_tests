import pages
import time
import pytest


class TestLogInPage:
    
    @pytest.mark.log_in_page_test()
    def test_log_in_page(self, page):
        pages.index_page.open_index_page(page)
        pages.log_in_page.open_log_in_page(page)
        pages.log_in_page.filling_log_in_form(page)
        pages.log_in_page.should_be_successful_login_text(page)