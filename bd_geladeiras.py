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


def listar_precoCresc():
    sql = "SELECT * FROM geladeiras ORDER BY preco;"
    cursor.execute(sql)
    return cursor.fetchall()

def preco_LG():
    sql = "SELECT preco FROM geladeiras WHERE marca = 'lg'"
    cursor.execute(sql)
    preco = cursor.fetchall()
    return preco

def preco_Pana():
    sql = "SELECT preco FROM geladeiras WHERE marca = 'panasonic'"
    cursor.execute(sql)
    preco = cursor.fetchall()
    return preco

def preco_Elec():
    sql = "SELECT preco FROM geladeiras WHERE marca = 'electrolux'"
    cursor.execute(sql)
    preco = cursor.fetchall()
    return preco

def preco_Brast():
    sql = "SELECT preco FROM geladeiras WHERE marca = 'brastemp'"
    cursor.execute(sql)
    preco = cursor.fetchall()
    return preco

def preco_Consu():
    sql = "SELECT preco FROM geladeiras WHERE marca = 'consul'"
    cursor.execute(sql)
    preco = cursor.fetchall()
    return preco
