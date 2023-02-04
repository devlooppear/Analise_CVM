# Estudo_CVM

- Esse código é uma automação criada para analise de dados relacionados com a Comissão de Valores Imobiliários (CVM). 

- Como usar: no arquivo principal "main.py", é executado o código e o bot coleta as informações e elas aparecem no Banco de Dados depois.

- O arquivo que executa o código é o ``main.py``.

- O output é a tabela no Banco de Dados.

## Ferramentas

- Foi usado o Sistema Gerenciador de Banco de Dados (SGBD): Postgres.

- Como configurar no Postgres: para a integração com o Postgres, o código Python deve estar com as informações de acesso coincidentes, podendo serem definidas na função ``IniciarPsycopg()``, como é ilustrado a baixo:

```python
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

    return cursor, conn
```

- Por isso, é possível tanto alterar essas informações para a integração, quanto criar o Banco de Dados (database)usuario 'postgres', senha 'postgres' e as outras informações, a não ser que tenham sido alteradas, já são as de padrão do postgres, como o 'localhost' e a posta escolhida ser '5432'.

## Bibliotecas

- Para utilizar o código, é necessário instalar as bibliotecas, com a escrita, no Terminal: pip install -r requirements.txt, que irá instalar todas as biblíotecas necessárias.

| Command | Description |
| --- | --- |
| pip install -r requirements.txt | Irá instalar todas as biblíotecas necessárias |