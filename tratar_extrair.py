from dateUts import *
from datetime import datetime as dt


def Tratar_Inserir(cursor_con,empresas,datas,relevantes,modalidades):
    for e, d, r, m in list(zip(empresas,datas,relevantes,modalidades)):
    
        d = d.text
        d = str(d)
        d = d.split()
        d.remove(d[1])
        for vlr in d:
            data = dt.strptime(vlr,'%d/%m/%Y')
            vlr = vlr.replace("/","-")
            vlr = vlr.split("-")

        r = r.text
        r = str(r)        


        m = m.text
        m = str(m)
                    

        e = e.text
        e = str(e)

        sql = f'''INSERT INTO cvm (empresa,data,fato_rel,modalidade) VALUES ('{e}',{dateToSql(data)},'{r}','{m}')'''
        cursor = cursor_con[0]
        cursor.execute(sql)
