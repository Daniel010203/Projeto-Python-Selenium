from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Instala o driver do Chrome e configura o serviço
servico = Service(ChromeDriverManager().install())

# Configura o navegador Chrome usando o serviço
navegador = webdriver.Chrome(service=servico)

# Agora você pode usar o navegador para navegar
navegador.get("https://www.netvasco.com.br/")

navegador.find_element()



