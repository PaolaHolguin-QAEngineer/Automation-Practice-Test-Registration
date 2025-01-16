from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    EMAIL_CREATE_INPUT = (By.ID, "email_create")
    SUBMIT_CREATE_BUTTON = (By.CSS_SELECTOR, "#SubmitCreate > span")
    ACCOUNT_CREATION_FORM = (By.ID, "account-creation_form")
    GENDER_FEMALE_RADIO = (By.ID, "id_gender2")
    FIRSTNAME_INPUT = (By.ID, "customer_firstname")
    LASTNAME_INPUT = (By.ID, "customer_lastname")
    PASSWORD_INPUT = (By.ID, "passwd")
    SUBMIT_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#submitAccount .icon-chevron-right")
