import sqlite3

# Conecte-se ao banco de dados (ou crie um se não existir)
conexao = sqlite3.connect('banco_de_dados.db')

# Crie um cursor para executar comandos SQL
cursor = conexao.cursor()

# Crie uma nova tabela
# cursor.execute('''
#     CREATE TABLE clientes (
#         id INTEGER PRIMARY KEY,
#         nome TEXT,
#         email TEXT,
#         endereço TEXT
#     )
# ''')

# Insira alguns dados na tabela
# cursor.execute("INSERT INTO clientes (nome, email, endereço) VALUES (?, ?, ?)", ('João', 'joao@email.com', 'Rua dos Joãozinhos'))
# cursor.execute("INSERT INTO clientes (nome, email, endereço) VALUES (?, ?, ?)", ('Maria', 'maria@email.com', 'Rua das Mariazinhas'))
# cursor.execute("INSERT INTO clientes (nome, email, endereço) VALUES (?, ?, ?)", ('Ana', 'ana@email.com', 'Rua das Aninhas'))
# cursor.execute("INSERT INTO clientes (nome, email, endereço) VALUES (?, ?, ?)", ('Pedro', 'pedro@email.com', 'Rua dos Pedrinhos'))
# cursor.execute("INSERT INTO clientes (nome, email, endereço) VALUES (?, ?, ?)", ('Joana', 'joana@email.com', 'Rua das Joaninhas'))
# cursor.execute("INSERT INTO clientes (nome, email, endereço) VALUES (?, ?, ?)", ('Luana', 'luana@email.com', 'Rua das Cachorras'))

#cursor.execute("UPDATE clientes SET endereço = ? WHERE nome = ?", ('Rua das Cadelas', 'Luana'))

cursor.execute("SELECT * FROM clientes WHERE id = 6", ())
cliente = cursor.fetchone()
print(cliente)

# Imprima os dados dos clientes
# cursor.execute("SELECT * FROM clientes")
# clientes = cursor.fetchall()
# for cliente in clientes:
#     print(cliente)

# Salve as alterações
conexao.commit()

# Feche a conexão
conexao.close()
