from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
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
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, f'//*[normalize-space(text())="{email}"]'
            )
        )
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, f'//*[normalize-space(text())="{name}"]'
            )
        )

    def test_delete(self):
        self.web_driver.get(
            f"{self.live_server_url}{reverse('user-detail', kwargs={'pk': 1})}"
        )
        self.web_driver.find_element(
            By.XPATH, '//button[normalize-space(text())="Delete"]'
        ).click()
        self.web_driver.find_element(By.CSS_SELECTOR, '.z-10 [type="submit"]').click()

        self.assertEqual(
            self.web_driver.current_url, f"{self.live_server_url}{reverse('user-list')}"
        )
        self.assertFalse(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="email1@email.com"]'
            )
        )
        self.assertFalse(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="name1"]'
            )
        )

    def test_read(self):
        self.web_driver.get(
            f"{self.live_server_url}{reverse('user-detail', kwargs={'pk': 1})}"
        )

        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="email1@email.com"]'
            )
        )
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="name1"]'
            )
        )

    def test_read_multiple(self):
        self.web_driver.get(f"{self.live_server_url}{reverse('user-list')}")

        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="email1@email.com"]'
            )
        )
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="name1"]'
            )
        )
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="email2@email.com"]'
            )
        )
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="name2"]'
            )
        )

    def test_read_multiple__filter(self):
        self.web_driver.get(f"{self.live_server_url}{reverse('user-list')}")
        self.web_driver.find_element(
            By.CSS_SELECTOR, '[name="email__icontains"]'
        ).send_keys("1")
        self.web_driver.find_element(
            By.CSS_SELECTOR, '[name="name__icontains"]'
        ).send_keys("1")
        self.web_driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="email1@email.com"]'
            )
        )
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="name1"]'
            )
        )
        self.assertFalse(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="email2@email.com"]'
            )
        )
        self.assertFalse(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="name2"]'
            )
        )

    def test_read_multiple__sort(self):
        self.web_driver.get(f"{self.live_server_url}{reverse('user-list')}")
        self.web_driver.find_element(
            By.XPATH, '//th//a[normalize-space(text())="Email"]'
        ).click()
        self.web_driver.find_element(
            By.XPATH, '//th//a[normalize-space(text())="Email"]'
        ).click()

        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH,
                '//*[normalize-space(text())="email9@email.com"]/following::*[normalize-space(text())="email8@email.com"]',
            )
        )

    def test_read_multiple__paginate(self):
        self.web_driver.get(f"{self.live_server_url}{reverse('user-list')}")
        self.web_driver.find_element(
            By.XPATH, '//a[*[normalize-space(text())="Next"]]'
        ).click()

        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="email11@email.com"]'
            )
        )
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="name11"]'
            )
        )
        self.assertFalse(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="email1@email.com"]'
            )
        )
        self.assertFalse(
            self.web_driver.find_elements(
                By.XPATH, '//*[normalize-space(text())="name1"]'
            )
        )

    def test_update(self):
        name = "name"

        self.web_driver.get(
            f"{self.live_server_url}{reverse('user-update', kwargs={'pk': 1})}"
        )
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="name"]').clear()
        self.web_driver.find_element(By.CSS_SELECTOR, '[name="name"]').send_keys(name)
        self.web_driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        self.assertEqual(
            self.web_driver.current_url,
            f"{self.live_server_url}{reverse('user-detail', kwargs={'pk': 1})}",
        )
        self.assertTrue(
            self.web_driver.find_elements(
                By.XPATH, f'//*[normalize-space(text())="{name}"]'
            )
        )
