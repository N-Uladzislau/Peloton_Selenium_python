from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import helpers as H
import time
import unittest
import HtmlTestRunner
# import AllureReports

class ChromeSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1_create_account(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Open Browser
        driver.get(H.peloton_ulr)
        print("______________Positive_Test____________\n"
              "Test 1 Create Account on website 'https://www.onepeloton.com/'")
        # Wait from 1s-3s
        H.delay1_3()
        # check API use -> POM
        H.check_API(driver)
        # check title on the main menu
        H.assert_title(driver, H.peloton_title)
        # close cookies
        driver.find_element(By.ID, "onetrust-close-btn-container").click()
        time.sleep(2)
        # Check Main Logo
        H.main_logo(driver)
        # Create Account
        H.create_account(driver)
        time.sleep(4)

    def test_2_add_bike(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get(H.peloton_ulr)
        print("_____________Positive_test______________\n"
              " Test 2 Add Bike to cart ")
        H.delay1_3()
        # Check API
        H.check_API(driver)
        # check Title
        H.assert_title(driver, H.peloton_title)
        # Check Main Logo
        H.main_logo(driver)
        # bikes button
        wait.until(EC.visibility_of_element_located((By.XPATH, H.BIKES)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.BIKES)))
        driver.find_element(By.XPATH, H.BIKES).click()
        time.sleep(3)
        # get src of IMG "Peloton Bike"
        print(driver.find_element(By.XPATH, '//*[@alt="Image of Peloton Bike"]').get_attribute("src"))
        # "Shop Bike" button  visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Shop Bike"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Shop Bike"]')))
        # Click on button
        driver.find_element(By.XPATH, '//*[text()="Shop Bike"]').click()
        time.sleep(2)
        H.assert_title(driver, 'Peloton® | Shop the Original Peloton Bike')
        # verify that description present on web page
        driver.find_element(By.XPATH, '//*[contains(text(),"Find the Bike package that")]')
        # Verify that "Bike basics" visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Bike Basics"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Bike Basics"]')))
        # click on "Bike Basics"
        driver.find_element(By.XPATH, '//*[text()="Bike Basics"]').click()
        time.sleep(3)
        # assert that "Bike Basics" present on the page
        self.assertIn('Bike Basics', driver.page_source)
        # "add to card" button visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Add to cart"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add to cart"]')))
        # click on "Add to cart" button
        driver.find_element(By.XPATH, '//*[text()="Add to cart"]').click()
        time.sleep(3)
        # verify that item was added to cart
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Your cart"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Your cart"]')))
        # verify "Checkout" button visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Checkout"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Checkout"]')))
        # click on "Checkout button"
        driver.find_element(By.XPATH, '//*[text()="Checkout"]').click()
        time.sleep(5)
        # Enter information for payment
        H.info_payment(driver)
        time.sleep(1)
        print("______________Test_Passed___________"
              "User able to buy a Bike ")


    def tearDown(self):
        self.driver.quit()
