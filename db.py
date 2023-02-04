
def Criacao_DB(cursor_con):
    cursor = cursor_con[0]
    sql = 'DROP TABLE IF EXISTS cvm'
    cursor.execute(sql)

    sql = f'''CREATE TABLE cvm(
    id SERIAL NOT NULL,
    empresa VARCHAR (100) NOT NULL,
    data DATE NOT NULL,
    fato_rel VARCHAR (100) NOT NULL,
    modalidade CHAR (15) NOT NULL,
    PRIMARY KEY (id)
    );'''
    cursor.execute(sql)