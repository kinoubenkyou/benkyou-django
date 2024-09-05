from selenium.webdriver.common.by import By

from main.tests.sign_in_mixin import SigninMixin


class SwitchOrganizationMixin(SigninMixin):
    fixtures = SigninMixin.fixtures + ["switch_organization_mixin"]

    def switch_organization(self):
        self.web_driver.find_element(By.XPATH, '//option[@value="1"]').click()
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
