import time
import re

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from task2 import open_personal_details, fill_personal_details, upload_file, delete_attachment, find_button_by_icon, \
    download_attachment, fill_and_save_comment
from task3 import enter_recruitment_page, fill_recruitment_columns, upload_file1, fill_other_columns_and_save, \
    shortlist_candidate, schedule_interview
from task4 import go_to_buzz_page, write_upload_and_share, write_comment, edit_post, delete_post
from task5 import enter_predefined_report_page, write_and_pick_report, select_items_and_click_button, \
    toggle_all_switches, click_on_save_button


def login(driver):
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "orangehrm-login-button")))

    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()


def add_new_employee(driver, add_employee_url):
    try:
        driver.get(add_employee_url)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "firstName")))

        driver.find_element(By.NAME, "firstName").send_keys("Steve")
        driver.find_element(By.NAME, "lastName").send_keys("Jones")

        id_input = driver.find_element(By.XPATH, "//div[@data-v-957b4417]//input[@class='oxd-input oxd-input--active']")

        id_input.send_keys("135")

        photo_input = driver.find_element(By.XPATH, "//input[@type='file']")
        photo_input.send_keys(r"")

        switch_label = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@class='']")))

        switch_label.click()

        username_input = driver.find_element(By.XPATH,
                                             "//input[@class='oxd-input oxd-input--active' and @autocomplete='off']")

        username_input.send_keys("your_username")

        password_input = driver.find_element(By.XPATH,
                                             "//div[@data-v-957b4417]//input[@class='oxd-input oxd-input--active' and "
                                             "@type='password']")

        password_input.send_keys("your_password1")

        confirm_password_input = driver.find_element(By.XPATH,
                                                     "//div[@data-v-957b4417]//input[@class='oxd-input "
                                                     "oxd-input--active' and @type='password']")
        confirm_password_input.send_keys("your_password1")

        save_button = driver.find_element(By.XPATH, "//button[contains(., 'Save')]")
        save_button.click()

        # Wait for success message
        time.sleep(10)
    except Exception as e:
        print("Error adding new employee:", e)


def fill_job_information(driver, job_section_url, emp_number):
    driver.get(job_section_url)

    try:
        # Wait for the job section page to load
        date_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-v-957b4417] input[data-v-1f99f73c][data-v-4a95a2e0]")))

        date_input.send_keys("2025-11-29")

        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"(//div[@class='oxd-select-text oxd-select-text--active' and @data-v-67d2aedf=''])[1]")))
        dropdown.click()
        action_chains = ActionChains(driver)
        action_chains.send_keys('q').send_keys(Keys.ENTER).perform()
        time.sleep(1)

        second_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"(//div[@class='oxd-select-text oxd-select-text--active' and @data-v-67d2aedf=''])[2]")))
        second_dropdown.click()

        ActionChains(driver).send_keys('q').send_keys(Keys.ENTER).perform()
        time.sleep(2)
        third_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"(//div[@class='oxd-select-text oxd-select-text--active' and @data-v-67d2aedf=''])[4]")))
        third_dropdown.click()

        ActionChains(driver).send_keys('f').send_keys('f').send_keys('f').send_keys(Keys.ENTER).perform()
        time.sleep(1)
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--secondary"))
        )

        save_button.click()
        time.sleep(2)
        # Navigate to the other website directly
        other_website_url = f"https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewReportToDetails/empNumber/{emp_number}"
        driver.get(other_website_url)
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button--medium")))
        add_button.click()
        # Find the text input and enter some text
        text_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
        text_input.send_keys("Odis  Adalwin")
        time.sleep(2)
        text_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        text_input.send_keys(Keys.ENTER)
        time.sleep(2)
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"(//div[@class='oxd-select-text oxd-select-text--active' and @data-v-67d2aedf=''])[1]")))
        dropdown.click()
        action_chains = ActionChains(driver)
        action_chains.send_keys('d').send_keys(Keys.ENTER).perform()
        time.sleep(2)
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--secondary"))
        )

        save_button.click()
    except Exception as e:
        print("Error filling job information:", e)


def navigate_to_employee_list(driver, employee_list_url):
    try:
        # Navigate to the provided employee list URL
        driver.get(employee_list_url)

        third_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"(//div[@class='oxd-select-text oxd-select-text--active' and @data-v-67d2aedf=''])[1]")))
        third_dropdown.click()
        time.sleep(2)
        action_chains = ActionChains(driver)
        action_chains.send_keys('f').send_keys('f').send_keys('f').send_keys(Keys.ENTER).perform()
        # Wait for the table to load
        save_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-button--secondary"))
        )

        save_button.click()
        # Find the element corresponding to "Steve Jones" in the table
        table_row = find_employee_in_table(driver, "Steve", "Jones")

        # Check if the expected values were found
        if table_row is None:
            print("Employee entry not found in the table")

    except Exception as e:
        print("Error finding:", e)


def find_employee_in_table(driver, first_name, last_name):
    try:
        # Find all rows in the table
        table_rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@class='oxd-table-row']")

        # Search for the specified employee in each row
        for row in table_rows:
            # Find the "First Name" element in the current row
            first_name_element = row.find_element(By.XPATH, ".//div[@class='header' and text()='First (& Middle) Name']"
                                                            "/following-sibling::div[@class='data']")

            # Find the "Last Name" element in the current row
            last_name_element = row.find_element(By.XPATH, ".//div[@class='header' and text()='Last Name']"
                                                           "/following-sibling::div[@class='data']")

            # Check if the current row matches the specified employee
            if first_name_element.text == first_name and last_name_element.text == last_name:
                return row  # Return the found row

        return None  # Return None if the employee is not found

    except Exception as e:
        print("Error finding employee in table:", e)
        return None  # Return None in case of an error


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Task 1: Login
    login(driver)

    # Add New Employee directly using the URL
    add_employee_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"
    add_new_employee(driver, add_employee_url)
    current_url = driver.current_url
    job_section_url = None
    emp_number = None

    match = re.search(r'/empNumber/(\d+)$', current_url)

    if match:
        emp_number = match.group(1)
        print(f"Extracted employee number: {emp_number}")
        job_section_url = f"https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewJobDetails/empNumber/{emp_number}"
    else:
        print("Employee number not found in the URL.")

    if job_section_url is not None:
        fill_job_information(driver, job_section_url, emp_number)
    else:
        print("Job information cannot be filled as job_section_url is not available.")
    employee_list_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    navigate_to_employee_list(driver, employee_list_url)
    print("1 Task Done")

    # Task 2
    open_personal_details(driver, emp_number)
    fill_personal_details(driver)
    upload_file(driver)

    file_name_to_download = ""
    download_attachment(driver, file_name_to_download)

    icon_class_to_find = "bi-pencil-fill"
    edit_button = find_button_by_icon(driver, icon_class_to_find)

    if edit_button:
        edit_button.click()
    else:
        print(f"Button with icon '{icon_class_to_find}' not found.")

    comment_text_to_fill = "This is a test comment."
    fill_and_save_comment(driver, comment_text_to_fill)

    file_name_to_delete = ""
    delete_attachment(driver, file_name_to_delete)
    print("2 Task Done")

    # Task3
    recruitment_url = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate"
    enter_recruitment_page(driver, recruitment_url)

    fill_recruitment_columns(driver)
    upload_file1(driver)
    fill_other_columns_and_save(driver)
    shortlist_candidate(driver)
    schedule_interview(driver)
    print("3 Task Done")

    # Task 4
    go_to_buzz_page(driver)

    write_upload_and_share(driver)
    edit_post(driver)
    write_comment(driver)
    delete_post(driver)
    print("4 Task Done")

    # Task 5
    enter_predefined_report_page(driver)

    write_and_pick_report(driver, 'g', 'm', [3])
    write_and_pick_report(driver, 'l', 'c', [4])
    time.sleep(1)
    select_items_and_click_button(driver, 'c', 1)
    select_items_and_click_button(driver, 'd', 1)
    select_items_and_click_button(driver, 'j', 1)
    toggle_all_switches(driver)
    click_on_save_button(driver)
    print("5 Task Done")

    time.sleep(15)
    driver.quit()
