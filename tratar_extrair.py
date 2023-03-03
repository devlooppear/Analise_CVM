from dateUts import *
from datetime import datetime


def Tratar_Inserir(cursor,empresas,datas,relevantes,modalidades):
    for empresa, data, relevante, modalidade in zip(empresas, datas, relevantes, modalidades):
        data_str = data.text.split()[0]
        data_obj = datetime.strptime(data_str, '%d/%m/%Y')
        data_sql = data_obj.strftime('%Y-%m-%d')
        relevante_str = relevante.text
        modalidade_str = modalidade.text
        empresa_str = empresa.text
        sql = 'INSERT INTO cvm (empresa, data, fato_rel, modalidade) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, (empresa_str, data_sql, relevante_str, modalidade_str))
