from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import requests

def before_all(context):
    # Configurar URLs base
    context.base_url = "https://projetofinal.jogajuntoinstituto.org"
    context.api_base_url = "https://apipf.jogajuntoinstituto.org"

    # Configurar WebDriver
    options = Options()
    context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    # Configurar sessão de API
    context.session = requests.Session()
    login_data = {"email": "dionebraga.work@gmail.com", "password": "123456"}
    response = context.session.post(f"{context.api_base_url}/login", json=login_data)
    if response.status_code == 200:
        token = response.json().get("token")
        context.session.headers.update({"Authorization": f"Bearer {token}"})
    else:
        raise Exception("Falha ao autenticar na API.")

def after_all(context):
    # Fechar WebDriver
    context.driver.quit()
