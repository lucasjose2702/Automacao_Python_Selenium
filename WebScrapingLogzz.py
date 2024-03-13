from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Iniciar o driver
driver = webdriver.Chrome()
driver.get("https://app.logzz.com.br/login")
campo_email = driver.find_element(By.XPATH,"//input[@id='email']").send_keys("XXXXXXXX")
campo_senha = driver.find_element(By.XPATH,"//input[@id='password']").send_keys("XXXXXXXX")
# Recaptcha e submit feito manualmente

time.sleep(90)

# Etapa de acessar pedidos e escolher filtros. Time.sleep mais logo processo está sendo feito manualmente.
# driver.get("https://app.logzz.com.br/pedidos/")

# Encontrar e clicar nos links para ver informações detalhadas do pedido
links = driver.find_elements(By.XPATH, "//a[@title='Ver detalhes do Pedido']")
textos_h2 = []
textos_h6 = []

for link in links:
    link.click()
    time.sleep(3)
    
    # Alterna o foco para a nova aba 
    driver.switch_to.window(driver.window_handles[-1])
    
    # Coleta o número de pedido do cliente 
    pedidos_h2 = driver.find_elements(By.CSS_SELECTOR, "h2")
    for h2_element in pedidos_h2:
        textos_h2.append(h2_element.text)
    
    # Coleta o nome do cliente
    name_clientes = driver.find_elements(By.XPATH, "//h6[contains(text(), 'Cliente')]/following-sibling::div/strong")
    for cliente_element in name_clientes:
        textos_h6.append(cliente_element.text)

    # Feche a aba atual 
    driver.close()

    # Volte à primeira aba original
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

# Fechar o driver
driver.quit()

# printa intem por intem atraves do loop
for item in textos_h2:
    # Remova a palavra 'Pedido #' e o espaço
    item_without_pedido = item.replace('Pedido #', '')  
    print(item_without_pedido)

for texto in textos_h6:
    print(texto)

