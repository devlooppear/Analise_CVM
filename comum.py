from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import psycopg2

def Browser():

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    return navegador

def Psycopg():

    conn = psycopg2.connect(
        database="Estudo_CVM",
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
        )
        
    conn.autocommit = True

    cursor = conn.cursor()

    return cursor