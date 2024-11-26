from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime as dt


def get_driver():
    # Opciones para hacer la navegación más fácil.
    options = webdriver.ChromeOptions()
    # En el navegador, deshabilita las barras de información, porque
    # pueden interferir con el script.
    options.add_argument("disable-infobars")
    # Para arrancar el navegador maximizado.
    options.add_argument("start-maximized")
    # Evita algunos problemas que ocurren cuando se interactúa con un
    # navegador en un ordenador con Linux.
    options.add_argument("disable-dev-shm-usage")
    # Por seguridad, los navegadores usan sandboxing. Si queremos que
    # nuestros scripts tengan mayores privilegios en la web a la que
    # accedemos para hacer scraping, lo deshabilitamos.
    options.add_argument("no-sandbox")
    # Estas opciones experimentales ayudan a Selenium a no ser detectado por
    # el navegador.
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Para evitar que se cierre el navegador (comentar cuando ya no sea necesario)
    options.add_experimental_option("detach", True)
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    
    # Esta es la página a la que queremos hacer scraping.
    driver.get("https://sso.vaadin.com/login?service=https://vaadin.com/login/cas")
    return driver


def main():
    driver = get_driver()
    # Pulsamos para hacer login con email
    driver.find_element(by=By.CLASS_NAME, value="mdc-button-email").click()
    # Accedemos por id, y enviamos keys (entradas de teclado) para el usuario
    driver.find_element(by=By.ID, value="email").send_keys("myuser@gmail.com")
    # Damos un tiempo de 2sg entre las operaciones de informar el usuario y la contraseña
    time.sleep(2)
    # Accedemos por id, y enviamos keys (entradas de teclado) para la contraseña y pulsamos Intro
    # También se muestra que en vez de By.ID se puede indicar texto con el valor directamente.
    driver.find_element(by="id", value="password-field").send_keys("mypassword" + Keys.RETURN)
    # Pulsamos el enlace
    element = driver.find_element(by=By.XPATH, value="//li[@class='v-footer-nav-link']/a[text()='Whistleblowing']")
    href = element.get_attribute("href")
    driver.get(href)


main()