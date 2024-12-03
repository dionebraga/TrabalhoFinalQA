from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que eu estou na página de login')
def step_open_login_page(context):
    context.driver.get(f"{context.base_url}/login")

@when('eu insiro credenciais válidas')
def step_enter_credentials(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    ).send_keys("dionebraga.work@gmail.com")
    context.driver.find_element(By.NAME, "password").send_keys("123456")
    context.driver.find_element(By.XPATH, "//button[text()='Iniciar sessão']").click()

@then('eu devo ser redirecionado para o dashboard')
def step_check_dashboard(context):
    dashboard_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "dashboard"))
    )
    assert dashboard_element.is_displayed()
