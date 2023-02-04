from selenium.webdriver.common.by import By
from time import sleep
def Extrair_Empresas(navegador):
    sleep(1)
    navegador.get(f"https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx")
    sleep(1)
    empresas = []
    sleep(1)
    busca_empresa = navegador.find_elements(By.XPATH, '//*[@id="grdDocumentos"]//tbody//tr//td[2]')

    for empresa in busca_empresa:
        empresas.append(empresa)
    return empresas

def Extrair_Datas(navegador):
    datas = []
    busca_datas = navegador.find_elements(By.XPATH, '//*[@id="grdDocumentos"]//tbody//tr//td[7]')

    for data in busca_datas:
        datas.append(data)
    return datas

def Extrair_Relevantes(navegador):
    relevantes = []
    busca_relevantes = navegador.find_elements(By.XPATH, '//*[@id="grdDocumentos"]/tbody/tr/td[3]')

    for relevante in busca_relevantes:
        relevantes.append(relevante)
    return relevantes

def Extrair_Modalidades(navegador):
    modalidades = []

    busca_modalidades = navegador.find_elements(By.XPATH, '//*[@id="grdDocumentos"]/tbody/tr/td[10]')

    for modalidade in busca_modalidades:
        modalidades.append(modalidade)
    return modalidades

