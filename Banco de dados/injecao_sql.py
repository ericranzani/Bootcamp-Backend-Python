import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente: ")
# forma incorreta de ser fazer, ter como base oque foi feito durente o curso arquivo dbapi
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
