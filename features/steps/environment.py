from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    """
    Este método é executado antes de todos os cenários.
    Ele inicializa o WebDriver e o armazena no contexto.
    """
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

def after_all(context):
    """
    Este método é executado após todos os cenários.
    Ele encerra o WebDriver.
    """
    context.driver.quit()
