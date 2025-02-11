from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def open_personal_details(driver, emp_number):
    personal_details_url = f"https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/{emp_number}"

    driver.get(personal_details_url)


def fill_personal_details(driver):
    try:
        time.sleep(3)

        nickname_input_div = driver.find_elements(By.CSS_SELECTOR, "div[data-v-957b4417] input[data-v-1f99f73c='']")[3]
        nickname_input_div.send_keys("StevenJ")

        other_id_input_div = driver.find_elements(By.CSS_SELECTOR, "div[data-v-957b4417] input[data-v-1f99f73c='']")[5]
        other_id_input_div.send_keys("0987")

        license_plate_input_div = \
            driver.find_elements(By.CSS_SELECTOR, "div[data-v-957b4417] input[data-v-1f99f73c='']")[6]
        license_plate_input_div.send_keys("ABC123")

        license_expiry_date_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "input.oxd-input.oxd-input--active[placeholder*='yyyy-mm-dd']"))
        )

        license_expiry_date_input.clear()
        license_expiry_date_input.send_keys("2024-03-03")

        ssn_number_input_div = driver.find_elements(By.CSS_SELECTOR, "div[data-v-957b4417] input[data-v-1f99f73c='']")[
            8]
        ssn_number_input_div.send_keys("55667")

        sin_number_input_div = driver.find_elements(By.CSS_SELECTOR, "div[data-v-957b4417] input[data-v-1f99f73c='']")[
            9]
        sin_number_input_div.send_keys("857396")
        time.sleep(3)

        save_button = driver.find_element(By.CLASS_NAME, "oxd-button--secondary")
        save_button.click()
        time.sleep(3)
    except Exception as e:
        print(f"Error filling personal details: {e}")


def upload_file(driver):
    try:
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[@class='oxd-button oxd-button--medium oxd-button--text' and "
                                        "@data-v-10d463b7]"))
        )
        add_button.click()
        time.sleep(3)

        file_input = driver.find_element(By.XPATH, "//input[@type='file']")

        file_input.send_keys(r"")
        time.sleep(2)
        save_button = driver.find_element(By.XPATH, "(//div[@class='oxd-form-actions']//button)[4]")
        save_button.click()
        time.sleep(5)

    except Exception as e:
        print(f"Error uploading file: {e}")


def download_attachment(driver, file_name):
    try:
        download_button_xpath = (f"//div[contains(@class, 'oxd-table-card') and .//div[text()='{file_name}']]//button["
                                 f"contains(@class, 'oxd-icon-button') and .//i[@class='oxd-icon bi-download']]")
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, download_button_xpath))
        )
        download_button.click()
        time.sleep(5)

    except Exception as e:
        print(f"Error downloading file '{file_name}': {e}")


def delete_attachment(driver, file_name):
    try:
        delete_button_xpath = (f"//div[contains(@class, 'oxd-table-card') and .//div[text()='{file_name}']]//button["
                               f"contains(@class, 'oxd-icon-button') and .//i[@class='oxd-icon bi-trash']]")
        delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )
        delete_button.click()
        time.sleep(2)

        confirmation_button = driver.find_element(By.CSS_SELECTOR,
                                                  "div.orangehrm-modal-footer button.oxd-button--label-danger")
        confirmation_button.click()

        time.sleep(5)
    except Exception as e:
        print(f"Error deleting file '{file_name}': {e}")


def find_button_by_icon(driver, icon_class):
    try:
        button_css = f"button i.{icon_class}"
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, button_css)))

        return button

    except Exception as e:
        print(f"Error finding button with icon '{icon_class}': {e}")
        return None


def fill_and_save_comment(driver, comment_text):
    try:
        textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[contains(@class, 'oxd-textarea--active') and "
                                                      "contains(@class, 'oxd-textarea--resize-vertical') and "
                                                      "contains(@data-v-bd337f32, '')]"))
        )

        textarea.clear()
        textarea.send_keys(comment_text)
        textarea.send_keys(comment_text)

        time.sleep(3)
        save_button = driver.find_element(By.XPATH, "(//div[@class='oxd-form-actions']//button)[4]")
        save_button.click()
        time.sleep(4)
    except Exception as e:
        print(f"Error filling and saving comment: {e}")
