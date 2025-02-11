from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time


def enter_recruitment_page(driver, recruitment_url):
    try:
        driver.get(recruitment_url)

    except Exception as e:
        print("Error entering recruitment page:", e)


def fill_recruitment_columns(driver):
    try:
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.orangehrm-firstname"))
        )

        first_name_input.send_keys("Ryan")

        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.orangehrm-lastname"))
        )

        last_name_input.send_keys("Gosling")

        third_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"(//div[@class='oxd-select-text oxd-select-text--active' and @data-v-67d2aedf=''])[1]")))
        third_dropdown.click()
        time.sleep(2)
        action_chains = ActionChains(driver)
        action_chains.send_keys('s').send_keys(Keys.ENTER).perform()

        time.sleep(2)

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-v-957b4417] input[placeholder='Type here']"))
        )

        email_input.send_keys("ryan@example.com")
        time.sleep(1)

    except Exception as e:
        print("Error filling recruitment columns:", e)


def upload_file1(driver):
    try:
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-v-957b4417] input[type='file']"))
        )

        file_input.send_keys(r"")
        time.sleep(2)

    except Exception as e:
        print("Error uploading file:", e)


def fill_other_columns_and_save(driver):
    try:
        notes_textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Type here']"))
        )

        notes_textarea.send_keys("This is a sample note.")

        time.sleep(2)

        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.oxd-button--secondary"))
        )
        WebDriverWait(driver, 10).until(EC.visibility_of(save_button))

        driver.execute_script("arguments[0].scrollIntoView();", save_button)

        save_button.click()
        time.sleep(5)

    except Exception as e:
        print("Error filling other columns and saving:", e)


def shortlist_candidate(driver):
    try:
        shortlist_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--success"))
        )

        shortlist_button.click()
        time.sleep(2)

        notes_textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[data-v-bd337f32]"))
        )

        notes_textarea.send_keys("This is a note text!")
        time.sleep(3)
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--secondary"))
        )

        save_button.click()
        time.sleep(3)

    except Exception as e:
        print("Error shortlisting candidate:", e)


def schedule_interview(driver):
    try:
        schedule_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--success"))
        )
        schedule_button.click()
        time.sleep(3)
        new_input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "(//div[@data-v-957b4417]//input[@class='oxd-input oxd-input--active' and @data-v-1f99f73c])[5]")
            )
        )

        new_input_field.send_keys("Your New Value")
        autocomplete_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active' and "
                 "@data-v-75e744cd]//input[@data-v-75e744cd]")
            )
        )
        autocomplete_input.send_keys("Odis  Adalwin")
        time.sleep(2)
        autocomplete_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        autocomplete_input.send_keys(Keys.ENTER)
        date_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-v-4a95a2e0] input"))
        )

        date_input.send_keys("2025-11-01")
        time.sleep(1)
        time_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-v-77385e33] input"))
        )

        time_input.send_keys("14:30")  # Replace with the actual time

        notes_textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[data-v-bd337f32]"))
        )

        notes_textarea.send_keys("Interview notes: Technical skills assessment")
        time.sleep(3)
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--secondary"))
        )


        save_button.click()
        time.sleep(3)

    except Exception as e:
        print("Error scheduling interview:", e)
