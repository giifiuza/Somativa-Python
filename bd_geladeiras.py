from conexao import conexao, cursor

def inserir_modelos(marca, modelo, preco_final):
    sql = f"""INSERT INTO geladeiras(marca, modelo, preco)
    values  ('{marca}','{modelo}', '{preco_final}');"""
    cursor.execute(sql)
    conexao.commit()

def scrape():
    sql = "truncate table geladeiras;"
    cursor.execute(sql)
    conexao.commit()

def select_marca():
    sql = 'select * from geladeiras where marcas="{}"'
