import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connection_status(driver):
    if(wait_for_element_exists(driver,By.XPATH,"//*[text()='Connected']")):
        logging.info("Status: Connected!")
    elif(wait_for_element_exists(driver,By.XPATH,"//*[text()='Disconnected']")):
        logging.warning("Status: Disonnected!")
    else:
        logging.warning("Status: Unknown!")

def check_active_element(driver):
    try:
        wait_for_element(driver,By.XPATH,"//*[text()='Activated']")
        driver.find_element(By.XPATH, "//*[text()='Activated']")
        logging.info("Extension is activated!")
    except NoSuchElementException:
        logging.error("Failed to find 'Activated' element. Extension activation failed.")

def wait_for_element_exists(driver, by, value, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        return True
    except TimeoutException as e:
        return False

def wait_for_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        return element
    except TimeoutException as e:
        logging.error(f"Error waiting for element {value}: {e}")
        raise

def add_cookie_to_local_storage(driver, cookie_value):
    driver.execute_script(f"window.localStorage.setItem('np_webapp_token', '{cookie_value}');")
    driver.execute_script(f"window.localStorage.setItem('np_token', '{cookie_value}');")
    logging.info(f"Added cookie with value {cookie_value[:8]}... to local storage.")

def run():
    setup_logging()
    version = '1.0.1'
    logging.info(f"Starting the script {version}...")

    # Read variables from the OS env
    extension_id = os.getenv('EXTENSION_ID')
    extension_url = os.getenv('EXTENSION_URL')
    cookie = os.getenv('NP_COOKIE')

    # Check if credentials are provided
    if not cookie:
        logging.error('No cookie provided. Please set the NP_COOOKIE environment variable.')
        return  # Exit the script if credentials are not provided

    chrome_options = Options()
    chrome_options.add_extension(f'./{extension_id}.crx')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    # NodePass checks for width less than 1024p
    driver.set_window_size(1024, driver.get_window_size()['height'])

    try:
        # Navigate to a webpage
        logging.info(f'Navigating to {extension_url} website...')
        driver.get(extension_url)

        add_cookie_to_local_storage(driver, cookie)
        
        # Check successful login
        while not wait_for_element_exists(driver,By.XPATH,"//*[text()='Dashboard']"):
            logging.info('Refreshing page to check login information...')
            driver.get(extension_url)

        logging.info('Logged in successfully!')

        logging.info('Accessing extension settings page...')
        driver.get(f'chrome-extension://{extension_id}/index.html')
        
        # Refresh until the "Login" button disappears
        while wait_for_element_exists(driver,By.XPATH,"//*[text()='Login']"):
            logging.info('Clicking the extension login button...')
            login = driver.find_element(By.XPATH, "//*[text()='Login']")
            login.click()
            time.sleep(10)
            # Refresh the page
            driver.refresh()
        
        # Check for the "Activated" element
        check_active_element(driver)

        # Get handles for all windows
        all_windows = driver.window_handles

        # Get the handle of the active window
        active_window = driver.current_window_handle

        # Close all windows except the active one
        for window in all_windows:
            if window != active_window:
                driver.switch_to.window(window)
                driver.close()

        # Switch back to the active window
        driver.switch_to.window(active_window)

        connection_status(driver)
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        logging.error(f'Restarting in 60 seconds...')
        driver.quit()
        time.sleep(60)
        run()

    while True:
        try:
            time.sleep(600)
            driver.refresh()
            connection_status(driver)
        except KeyboardInterrupt:
            logging.info('Stopping the script...')
            driver.quit()
            break

run()