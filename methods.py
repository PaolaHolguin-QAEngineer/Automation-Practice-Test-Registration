from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)  # Tiempo de espera explícito

    def fill_input_field(self, locator, value):
        """Rellena un campo de texto."""
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)

    def click_element(self, locator):
        """Hace clic en un elemento."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def select_dropdown_option(self, locator, value):
        """Selecciona una opción en un menú desplegable."""
        dropdown = Select(self.wait.until(EC.element_to_be_clickable(locator)))
        dropdown.select_by_visible_text(value)

    def wait_for_element(self, locator):
        """Espera a que un elemento esté presente en la página."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator):
        """Verifica si un elemento es visible en la página."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:  # Manejar el caso cuando el elemento no está visible
            return False