#Importando SQLite
import sqlite3 as lite

# Criando conn
conn = lite.connect('dadosCRUD.db')

#Criando tabela
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado_consulta TEXT, assunto TEXT)')