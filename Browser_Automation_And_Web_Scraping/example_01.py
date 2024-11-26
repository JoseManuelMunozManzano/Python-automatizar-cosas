from selenium import webdriver
from selenium.webdriver.common.by import By


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
    driver.get("http://automated.pythonanywhere.com")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[1]")
    return element.text


print(main())