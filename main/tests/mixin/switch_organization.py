from selenium.webdriver.common.by import By

from main.tests.mixin import SignInMixin


class SwitchOrganizationMixin(SignInMixin):
    fixtures = [*SignInMixin.fixtures, "switch_organization_mixin"]

    def switch_organization(self):
        self.web_driver.find_element(By.XPATH, '//option[@value="1"]').click()
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
