import Data
from selenium import webdriver
from Locators import RegistrationPageLocators
from methods import BasePage


class TestRegistrationAutomationPractice:
    def setup_method(self):
        """Inicialización del navegador."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_page = BasePage(self.driver)

    def teardown_method(self):
        """Cierre del navegador."""
        self.driver.quit()

    def test_registration(self):
        """Caso de prueba: Registro en Automation Practice."""
        # Navegar al sitio
        self.driver.get(Data.base_url)

        # Crear cuenta
        self.base_page.fill_input_field(RegistrationPageLocators.EMAIL_CREATE_INPUT, Data.email)
        self.base_page.click_element(RegistrationPageLocators.SUBMIT_CREATE_BUTTON)

        # Esperar a que el formulario esté disponible
        self.base_page.wait_for_element(RegistrationPageLocators.ACCOUNT_CREATION_FORM)

        # Completar formulario de registro
        self.base_page.click_element(RegistrationPageLocators.GENDER_FEMALE_RADIO)
        self.base_page.fill_input_field(RegistrationPageLocators.FIRSTNAME_INPUT, Data.firstname)
        self.base_page.fill_input_field(RegistrationPageLocators.LASTNAME_INPUT, Data.lastname)
        self.base_page.fill_input_field(RegistrationPageLocators.PASSWORD_INPUT, Data.password)

        # Confirmar registro
        self.base_page.click_element(RegistrationPageLocators.SUBMIT_ACCOUNT_BUTTON)

