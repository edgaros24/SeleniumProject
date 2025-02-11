from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def go_to_buzz_page(driver):
    buzz_url = "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"

    driver.get(buzz_url)


def write_upload_and_share(driver):
    try:

        time.sleep(3)
        share_photos_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[@class='oxd-glass-button' and contains(text(), 'Share Photos')]"))
        )
        share_photos_button.click()

        time.sleep(5)
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        file_input.send_keys(
            r"")

        time.sleep(5)
        share_button = driver.find_element(By.CSS_SELECTOR, "button[data-v-10d463b7][data-v-cbb80b9a]")
        share_button.click()

        time.sleep(4)

    except Exception as e:
        print(f"Error navigating to Buzz page and writing to textarea: {e}")


def edit_post(driver):
    try:
        three_dots_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-v-429cfcf3] button[data-v-f5c763eb]"))
        )
        three_dots_button.click()

        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.orangehrm-buzz-post-header-config-item i.bi-pencil"))
        )
        edit_button.click()

        textarea_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.orangehrm-buzz-post-modal-header-text textarea"))
        )
        textarea_modal.clear()
        textarea_modal.send_keys("I like cookies!")

        save_changes_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-v-10d463b7][data-v-cbb80b9a]"))
        )
        save_changes_button.click()

        time.sleep(10)

    except Exception as e:
        print(f"Error editing buzz post: {e}")


def write_comment(driver):
    try:
        comment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-v-f5c763eb][data-v-f9d19a8e]'))
        )

        comment_button.click()

        comment_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Write your comment..."]'))
        )

        comment_input.clear()
        comment_input.send_keys("Great!!!")
        comment_input.send_keys(Keys.RETURN)

        time.sleep(5)

        try:
            delete_comment_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//p[@class="oxd-text oxd-text--p orangehrm-post-comment-action" and text()="Delete"]'))
            )

            delete_comment_button.click()

            time.sleep(2)
            delete_confirmation_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'oxd-button--label-danger'))
            )

            delete_confirmation_button.click()

            time.sleep(3)

        except Exception as e:
            print(f"Error deleting comment: {e}")
    except Exception as e:
        print(f"Error writing comment: {e}")


def delete_post(driver):
    try:
        scroll_up(driver)
        three_dots_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-v-429cfcf3][data-v-061e7373] button['
                                                         'data-v-f5c763eb][data-v-061e7373]'))
        )
        three_dots_button.click()
        time.sleep(2)

        delete_post_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.orangehrm-buzz-post-header-config-item[data-v-061e7373] '
                                                         'p[data-v-7b563373][data-v-061e7373]'))
        )
        delete_post_option.click()

        time.sleep(2)

        delete_confirmation_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--label'
                                                         '-danger.orangehrm-button-margin[data-v-10d463b7]['
                                                         'data-v-64d94959]'))
        )
        delete_confirmation_button.click()
        time.sleep(3)
    except Exception as e:
        print(f"Error deleting post: {e}")


def scroll_up(driver):
    try:
        driver.execute_script("window.scrollTo(0, 0);")
    except Exception as e:
        print(f"Error scrolling up: {e}")
