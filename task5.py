import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def enter_predefined_report_page(driver):
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/definePredefinedReport")
        input_field_xpath = "//div[@data-v-957b4417]//input[@class='oxd-input oxd-input--active']"
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, input_field_xpath)))

        input_field.clear()

        input_field.send_keys("jduidjiugik")
    except Exception as e:
        print(f"Error entering predefined report page: {e}")


def write_and_pick_report(driver, key1, key2, key3):
    try:

        dropdown_xpath = "//div[@class='oxd-select-text oxd-select-text--active']"
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))

        dropdown.click()

        action_chains = ActionChains(driver)
        action_chains.send_keys(key1).send_keys(Keys.ENTER).perform()

        second_dropdown_xpath = "//div[@class='oxd-select-text oxd-select-text--active']"
        second_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, second_dropdown_xpath)))

        second_dropdown.click()

        action_chains = ActionChains(driver)
        action_chains.send_keys('c').send_keys('c').send_keys(Keys.ENTER).perform()

        button_xpath = "//button[@class='oxd-icon-button orangehrm-report-icon']"
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button.click()
        first_dropdown_xpath = f"(//div[@class='oxd-select-text oxd-select-text--active' and @data-v-67d2aedf='']){key3}"
        first_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, first_dropdown_xpath)))

        first_dropdown.click()
        time.sleep(1)
        action_chains = ActionChains(driver)
        action_chains.send_keys(key2).send_keys(Keys.ENTER).perform()
        time.sleep(2)

    except Exception as e:
        print(f"Error writing and picking report: {e}")


def select_items_and_click_button(driver, key_to_press1, button_index):
    try:
        first_dropdown_xpath = f"(//div[@class='oxd-select-text oxd-select-text--active' and @data-v-67d2aedf=''])[5]"
        first_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, first_dropdown_xpath)))

        first_dropdown.click()

        action_chains = ActionChains(driver)
        action_chains.send_keys(key_to_press1).send_keys(Keys.ENTER).perform()

        buttons_xpath = ("//button[contains(@class, 'oxd-icon-button') and contains(@class, 'orangehrm-report-icon') "
                         "and @type='button' and @data-v-f5c763eb='']")
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, buttons_xpath)))

        buttons[button_index].click()
        time.sleep(2)

    except Exception as e:
        print(f"Error interacting with dropdowns and button: {e}")


def toggle_all_switches(driver):
    try:
        switch_xpath = "//label[@data-v-8e4757dc]//input[@type='checkbox']"
        switches = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, switch_xpath)))

        for switch in switches:
            driver.execute_script("arguments[0].click();", switch)

    except Exception as e:
        print(f"Error toggling switches: {e}")


def click_on_save_button(driver):
    try:
        time.sleep(2)
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--secondary"))
        )

        save_button.click()
    except Exception as e:
        print(f"Error clicking on save button: {e}")
