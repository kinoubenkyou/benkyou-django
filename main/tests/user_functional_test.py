from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.utils.http import urlencode
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from main.models import User


class UserFunctionalTest(StaticLiveServerTestCase):
    fixtures = ["user"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        cls.web_driver = WebDriver(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.web_driver.quit()
        super().tearDownClass()

    def test_create(self):
        email = "email@email.com"
        name = "name"
        password = "dr0wss@p"

        self.web_driver.get(f"{self.live_server_url}{reverse('user-create')}")
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(email)
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="name"]').send_keys(name)
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="password2"]').send_keys(
            password
        )
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="password1"]').send_keys(
            password
        )
        self.web_driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}{reverse('user-detail', kwargs={'pk': User.objects.get(email=email, name=name).pk})}",
        )
        self.assertIn(email, self.web_driver.page_source)
        self.assertIn(name, self.web_driver.page_source)

    def test_delete(self):
        self.web_driver.get(
            f"{self.live_server_url}{reverse('user-detail', kwargs={'pk': 1})}"
        )
        self.web_driver.find_element(
            By.XPATH, '//button[normalize-space(text())="Delete"]'
        ).click()
        self.web_driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        self.assertEqual(
            self.web_driver.current_url, f"{self.live_server_url}{reverse('user-list')}"
        )
        self.assertNotIn("email1@email.com", self.web_driver.page_source)
        self.assertNotIn("name1", self.web_driver.page_source)

    def test_read(self):
        self.web_driver.get(
            f"{self.live_server_url}{reverse('user-detail', kwargs={'pk': 1})}"
        )

        self.assertIn("email1@email.com", self.web_driver.page_source)
        self.assertIn("name1", self.web_driver.page_source)

    def test_read_multiple(self):
        self.web_driver.get(f"{self.live_server_url}{reverse('user-list')}")

        self.assertIn("email1@email.com", self.web_driver.page_source)
        self.assertIn("name1", self.web_driver.page_source)
        self.assertIn("email2@email.com", self.web_driver.page_source)
        self.assertIn("name2", self.web_driver.page_source)

    def test_read_multiple__filter(self):
        self.web_driver.get(
            f"{self.live_server_url}{reverse('user-list')}?{urlencode({"email__icontains": "1", "name__icontains": "1"})}"
        )

        self.assertIn("email1@email.com", self.web_driver.page_source)
        self.assertIn("name1", self.web_driver.page_source)
        self.assertNotIn("email2@email.com", self.web_driver.page_source)
        self.assertNotIn("name2", self.web_driver.page_source)

    def test_read_multiple__sort(self):
        self.web_driver.get(
            f"{self.live_server_url}{reverse('user-list')}?{urlencode({"ordering": "-email"})}"
        )

        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH,
                '//*[contains(text(), "email2@email.com")]/following::*[contains(text(), "email1@email.com")]',
            )
        )

    def test_update(self):
        name = "name"

        self.web_driver.get(
            f"{self.live_server_url}{reverse('user-update', kwargs={'pk': 1})}"
        )
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="name"]').send_keys(name)
        self.web_driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}{reverse('user-detail', kwargs={'pk': 1})}",
        )
        self.assertIn(name, self.web_driver.page_source)
