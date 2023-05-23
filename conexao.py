import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='somativa',
    user='root',
    password=''
)

cursor = conexao.cursor()

