import config
import pages


class IndexPage:

    def open_index_page(self, page) -> None:
        pages.base_page.open_page(config.url.DOMIAN, page)