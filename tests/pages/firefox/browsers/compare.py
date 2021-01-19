# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import BasePage
from pages.regions.download_button import DownloadButton
from pages.regions.menu_list import MenuList
from pages.regions.sticky_promo import StickyPromo


class BrowserComparisonPage(BasePage):

    _URL_TEMPLATE = '/{locale}/firefox/browsers/compare/{slug}/'

    _primary_download_button_locator = (By.ID, 'download-button-thanks')
    _secondary_download_button_locator = (By.ID, 'download-secondary')
    _browser_menu_list_locator = (By.CSS_SELECTOR, '.mzp-c-menu-list.mzp-t-download')

    @property
    def primary_download_button(self):
        el = self.find_element(*self._primary_download_button_locator)
        return DownloadButton(self, root=el)

    @property
    def secondary_download_button(self):
        el = self.find_element(*self._secondary_download_button_locator)
        return DownloadButton(self, root=el)

    @property
    def browser_menu_list(self):
        el = self.find_element(*self._browser_menu_list_locator)
        return MenuList(self, root=el)

    def wait_for_page_to_load(self):
        el = self.find_element(By.TAG_NAME, 'html')
        self.wait.until(lambda s: 'loaded' in el.get_attribute('class'))
        promo = self.find_element(*self._sticky_promo_modal_content_locator)
        self.wait.until(lambda s: 'is-displayed' in promo.get_attribute('class'))
        return self

    @property
    def promo(self):
        return StickyPromo(self)
