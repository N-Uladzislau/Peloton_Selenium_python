import driver as driver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
actions = ActionChains(driver)
from selenium.webdriver.common.action_chains import ActionChains
import driver
import time
import random
import requests
from faker import Faker
F = Faker()
F.Number = Faker(["en_CA"])


# url for the main Website
peloton_ulr = "https://www.onepeloton.com/"
# Title on the main page
peloton_title = "Peloton® | Workouts Streamed Live & On-Demand"
# Logo on the main page
peloton_main_logo = '//*[@aria-label="Peloton home"]'
# Button Bikes
BIKES = "//button[@data-test-id='nav.bikes']"













# Time delay fun
def delay1_5():
    time.sleep(random.randint(1, 5))

def delay1_3():
    time.sleep(random.randint(1, 3))

# Check API
def check_API(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print(f"URL has : {requests.get(driver.current_url).status_code} as status")
    else:
        print("API has response code is not 200")

# Assert Driver title
def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print(f"Page has {driver.title} as Page title")
    # SCR of page of title if title is different
    driver.get_screenshot_as_file(f'Page has different {title}.png')
    if not title in driver.title:
        raise Exception(f"Page {title} has wrong title")

# Check the "Main Logo" is present
def main_logo(driver):
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, peloton_main_logo)))
        print("Logo is present and correct")
    except NoSuchElementException:
        print("Logo is NOT present on the Main Page")
        driver.get_screenshot_as_file("Page_has_different_Logo.png")

# Create Account
def create_account(driver):
    wait = WebDriverWait(driver, 10)
    # Verify that icon Log in / Create account is present and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-test-id="account"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-test-id="account"]')))
    # Click on icon in the right corner
    driver.find_element(By.XPATH, '//*[@data-test-id="account"]').click()
    # Verify that button "My Membership" is present and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="My membership"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="My membership"]')))
    # Click on button "My Membership"
    driver.find_element(By.XPATH, '//*[text()="My membership"]').click()
    # wait for switch tab
    time.sleep(3)
    # switch tab
    driver.switch_to.window(driver.window_handles[1])
    # Verify Title
    assert_title(driver, "Log in | Peloton")
    # Verify that "Log in" is present on page
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="Form__Title-sc-1bsx23q-4 zoLFw"]')))
    # Button "Sign up now." is present and clickable
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sign up now.')))
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign up now.')))
    driver.find_element(By.LINK_TEXT, 'Sign up now.').click()
    time.sleep(1)
    # Verify Title
    assert_title(driver, "Peloton® | Start Your Free App Membership")
    # Verify that "Create Account" is present on the page
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Create Account"]')))
    # placeholder "Email Address*" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    wait.until(EC.element_to_be_clickable((By.NAME, "email")))
    # Enter Email => use Faker library
    driver.find_element(By.NAME, 'email').send_keys(F.email())
    # "Get Started" button is present and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Get Started"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Get Started"]')))
    # Click on button "Get Started"
    driver.find_element(By.XPATH, '//*[text()="Get Started"]').click()
    # wait for loading page
    time.sleep(5)
    # Check text "Start your Peloton App Membership" is present on the page
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Start your Peloton App Membership"]')))
    # "SELECT YOUR BILLING PREFERENCE" Monthly and Annual button is clickable
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Monthly billing"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Annual billing"]')))
    # placeholder "Cardholder Name" is clickable
    wait.until(EC.element_to_be_clickable((By.NAME, 'creditCardName')))
    # switch to different frame for Credit Card
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Secure card number input frame']"))
    # placeholder "Credit Card Number" is clickable
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]')))
    # Check Box button
    # wait.until(EC.element_to_be_clickable((By.ID, 'membershipTermsAndConditionsFlag')))
    # Button "Start Your Membership"
    driver.switch_to.default_content()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='START YOUR MEMBERSHIP']")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='START YOUR MEMBERSHIP']")))
    print("User able to Create Account and get MemberShip\n"
          "test_passed")


# Enter information for payment (Use faker DATA)
def info_payment(driver):
    wait = WebDriverWait(driver, 10)
    # placeholder "Email Address*" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    wait.until(EC.element_to_be_clickable((By.NAME, "email")))
    # enter email
    driver.find_element(By.NAME, 'email').send_keys(F.email())
    time.sleep(1)
    # placeholder "firstName" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'firstName')))
    wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
    # enter FirstName
    driver.find_element(By.NAME, 'firstName').send_keys(F.first_name())
    time.sleep(1)
    # placeholder "lastName" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'lastName')))
    wait.until(EC.element_to_be_clickable((By.NAME, "lastName")))
    # enter LastName
    driver.find_element(By.NAME, 'lastName').send_keys(F.last_name())
    time.sleep(1)
    # placeholder "phone" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'phone')))
    wait.until(EC.element_to_be_clickable((By.NAME, "phone")))
    # Enter random phone
    driver.find_element(By.NAME, 'phone').send_keys(F.Number.phone_number())
    time.sleep(1)
    # placeholder "Address" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'shipping.address.line1')))
    wait.until(EC.element_to_be_clickable((By.NAME, "shipping.address.line1")))
    # Enter Address
    driver.find_element(By.NAME, 'shipping.address.line1').send_keys(F.street_address())
    time.sleep(1)
    # placeholder "Apt/Suite" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'line2')))
    wait.until(EC.element_to_be_clickable((By.NAME, "line2")))
    # Enter Apt/Suite
    driver.find_element(By.NAME, 'line2').send_keys(F.secondary_address())
    time.sleep(1)
    # placeholder "City" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'city')))
    wait.until(EC.element_to_be_clickable((By.NAME, "city")))
    # Enter City
    driver.find_element(By.NAME, 'city').send_keys(F.city())
    time.sleep(1)
    # placeholder "State" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'shipping.address.state')))
    wait.until(EC.element_to_be_clickable((By.NAME, "shipping.address.state")))
    # Enter State
    driver.find_element(By.NAME, 'shipping.address.state').send_keys(F.state_abbr())
    time.sleep(1)
    # placeholder "ZipCode" is present and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'postalCode')))
    wait.until(EC.element_to_be_clickable((By.NAME, "postalCode")))
    # Enter ZipCode
    driver.find_element(By.NAME, 'postalCode').send_keys(F.zipcode())
    time.sleep(1)

