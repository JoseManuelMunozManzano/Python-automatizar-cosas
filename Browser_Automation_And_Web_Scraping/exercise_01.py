from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
    # options.add_experimental_option("detach", True)
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    
    # Esta es la página a la que queremos hacer scraping.
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    # Accedemos por id, y enviamos keys (entradas de teclado) para el usuario
    driver.find_element(by=By.ID, value="id_username").send_keys("automated")
    # Damos un tiempo de 2sg entre las operaciones de informar el usuario y la contraseña
    time.sleep(2)
    # Accedemos por id, y enviamos keys (entradas de teclado) para la contraseña y pulsamos Intro
    # También se muestra que en vez de By.ID se puede indicar texto con el valor directamente.
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    # Mejor que time en este caso. Esperamos que aparezca el botón home
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/a')))
    # Pulsamos el botón home
    driver.find_element(by=By.XPATH, value="/html/body/nav/div/a").click()
    
    # Aparece la clase text-success cuando aparece la temperatura, así que espero a que
    # aparezca esa clase.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'text-success')))    
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)


print(main())