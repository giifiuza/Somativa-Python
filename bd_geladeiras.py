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


def select_marca(marca):
    sql = f'select * from geladeiras where marca="{marca}";'
    cursor.execute(sql)
    resultados = cursor.fetchall()
    return resultados


def listar_tudo():
    sql = "SELECT * FROM geladeiras;"
    cursor.execute(sql)
    return cursor.fetchall()
