from comum import Browser, Psycopg
from db import Criacao_DB
from extração import Extrair_Empresas, Extrair_Datas, Extrair_Relevantes, Extrair_Modalidades
from tratar_extrair import Tratar_Inserir

def main():

    navegador = Browser()
    cursor = Psycopg()
    Criacao_DB(cursor)
    empresas = Extrair_Empresas(navegador)
    datas = Extrair_Datas(navegador)
    relevantes = Extrair_Relevantes(navegador)
    modalidades = Extrair_Modalidades(navegador)
    Tratar_Inserir(cursor,empresas,datas,relevantes,modalidades)

main()