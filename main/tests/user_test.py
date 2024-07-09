from django.test import LiveServerTestCase
from django.urls import reverse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from main.models import User


class UserTest(LiveServerTestCase):
    fixtures = ['user']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        cls.web_driver = WebDriver(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.web_driver.quit()
        super().tearDownClass()

    def test_create(self):
        email = 'email@email.com'
        name = 'name'
        password = 'dr0wss@p'

        self.web_driver.get(f"{self.live_server_url}{reverse('user_create')}")
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(email)
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="name"]').send_keys(name)
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="password2"]').send_keys(password)
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="password1"]').send_keys(password)
        self.web_driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        self.assertEqual(self.web_driver.current_url, f"{self.live_server_url}{reverse('user', kwargs={'pk': User.objects.get(email=email, name=name).pk})}")
        self.assertTrue(email in self.web_driver.page_source)
        self.assertTrue(name in self.web_driver.page_source)

    def test_read(self):
        self.web_driver.get(f"{self.live_server_url}{reverse('user', kwargs={'pk': 1})}")

        self.assertTrue('email1@email.com' in self.web_driver.page_source)
        self.assertTrue('name1' in self.web_driver.page_source)

