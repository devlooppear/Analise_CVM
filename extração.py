from selenium.webdriver.common.by import By
from time import sleep

EMPRESA_XPATH = '//*[@id="grdDocumentos"]//tbody//tr//td[2]'
DATAS_XPATH = '//*[@id="grdDocumentos"]//tbody//tr//td[7]'
RELEVANTES_XPATH = '//*[@id="grdDocumentos"]/tbody/tr/td[3]'
MODALIDADES_XPATH = '//*[@id="grdDocumentos"]/tbody/tr/td[10]'

def Extrair_Empresas(navegador):
    sleep(1)
    navegador.get(f"https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx")
    sleep(1)
    busca_empresa = navegador.find_elements(By.XPATH, EMPRESA_XPATH)
    empresas = [empresa for empresa in busca_empresa]
    return empresas

def Extrair_Datas(navegador):
    datas = []
    busca_datas = navegador.find_elements(By.XPATH, DATAS_XPATH)

    for data in busca_datas:
        datas.append(data)
    return datas

def Extrair_Relevantes(navegador):
    relevantes = []
    busca_relevantes = navegador.find_elements(By.XPATH, RELEVANTES_XPATH)

    for relevante in busca_relevantes:
        relevantes.append(relevante)
    return relevantes

def Extrair_Modalidades(navegador):
    modalidades = []

    busca_modalidades = navegador.find_elements(By.XPATH, MODALIDADES_XPATH)

    for modalidade in busca_modalidades:
        modalidades.append(modalidade)
    return modalidades
