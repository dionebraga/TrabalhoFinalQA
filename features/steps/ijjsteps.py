import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def tirar_screenshot(context, nome_arquivo):
    """Salva uma captura de tela do estado atual do navegador."""
    context.driver.save_screenshot(nome_arquivo)

@given(u'que estou na página de contato do Instituto Joga Junto')
def step_impl(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get('https://www.jogajuntoinstituto.org/')
    
    # Scroll até a seção de contato
    contato_section = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nome'))
    )
    context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", contato_section)
    time.sleep(2)
    tirar_screenshot(context, '1_pagina_contato.png')


@when(u'preencho o formulário com "{nome}", "{email}", "{assunto}" e "{mensagem}"')
def step_impl(context, nome, email, assunto, mensagem):
    context.driver.find_element(By.ID, 'nome').send_keys(nome)
    context.driver.find_element(By.ID, 'email').send_keys(email)
    select_assunto = Select(context.driver.find_element(By.ID, 'assunto'))
    select_assunto.select_by_visible_text(assunto)
    context.driver.find_element(By.ID, 'mensagem').send_keys(mensagem)
    tirar_screenshot(context, '2_formulario_preenchido.png')


@when(u'clico no botão de enviar')
def step_impl(context):
    botao_enviar = context.driver.find_element(By.XPATH, '//*[@id="Contato"]/div[1]/form/button')
    context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao_enviar)
    time.sleep(1)
    botao_enviar.click()
    tirar_screenshot(context, '3_botao_enviar_clicado.png')


@then(u'vejo a mensagem "Mensagem enviada com sucesso" e fecho o navegador')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 5).until(EC.alert_is_present())
        alerta = context.driver.switch_to.alert
        print(f"Texto do alerta: {alerta.text}")
        alerta.accept()
    except Exception as e:
        print("Nenhum alerta encontrado:", e)
    
    time.sleep(2)
    tirar_screenshot(context, '4_resultado_final.png')
    context.driver.quit()
