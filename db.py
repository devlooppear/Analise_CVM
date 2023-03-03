
def Criacao_DB(cursor):

    sql = f'''CREATE TABLE cvm(
    id SERIAL NOT NULL,
    empresa VARCHAR (100) NOT NULL,
    data DATE NOT NULL,
    fato_rel VARCHAR (100) NOT NULL,
    modalidade CHAR (15) NOT NULL,
    PRIMARY KEY (id)
    );'''
    cursor.execute(sql)