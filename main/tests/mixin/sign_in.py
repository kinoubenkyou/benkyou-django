from selenium.webdriver.common.by import By


class SignInMixin:
    fixtures = ["sign_in_mixin"]

    def sign_in(self):
        self.web_driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(
            "email1@email.com",
        )
        self.web_driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(
            "dr0wss@p1",
        )
        self.web_driver.find_element(By.XPATH, '//*[@type="submit"]').click()
