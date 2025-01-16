from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class TestRegistrationAutomationPractice:
    def setup_method(self, method):
        """Inicialización del navegador."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # Tiempo de espera explícito

    def teardown_method(self, method):
        """Cierre del navegador."""
        self.driver.quit()

    def fill_input_field(self, by, locator, value):
        """Método auxiliar para rellenar campos de texto."""
        field = self.wait.until(EC.visibility_of_element_located((by, locator)))
        field.clear()
        field.send_keys(value)

    def select_dropdown_option(self, by, locator, value):
        """Método auxiliar para seleccionar opciones en un dropdown."""
        dropdown = Select(self.wait.until(EC.element_to_be_clickable((by, locator))))
        dropdown.select_by_visible_text(value)

    def test_registration(self):
        """Caso de prueba: Registro en Automation Practice."""
        base_url = "http://www.automationpractice.pl/index.php?controller=authentication&back=my-account"
        email = "abc125@xmail.com"
        firstname = "Paolo"
        lastname = "Holguin"
        password = "123abc"
        birth_day = "14"
        birth_month = "January"
        birth_year = "2005"

        # Navegar al sitio
        self.driver.get(base_url)
        print(f"URL actual: {self.driver.current_url}")  # Depuración

        # Crear cuenta
        self.fill_input_field(By.ID, "email_create", email)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#SubmitCreate > span"))).click()

        # Esperar a que el formulario esté disponible
        self.wait.until(EC.presence_of_element_located((By.ID, "account-creation_form")))

        # Completar formulario de registro
        self.wait.until(EC.element_to_be_clickable((By.ID, "id_gender2"))).click()
        self.fill_input_field(By.ID, "customer_firstname", firstname)
        self.fill_input_field(By.ID, "customer_lastname", lastname)

        # Confirmar que el selector de contraseña es correcto
        try:
            self.fill_input_field(By.ID, "passwd", password)  # Cambiado de "password" a "passwd"
        except Exception as e:
            self.driver.save_screenshot("debug_screenshot.png")  # Captura de pantalla en caso de fallo
            raise Exception(f"No se pudo interactuar con el campo de contraseña: {e}")
