import sqlite3

# Conecte-se ao banco de dados (ou crie um se não existir)
conexao = sqlite3.connect('meu_banco_de_dados.db')

# Crie um cursor para executar comandos SQL
cursor = conexao.cursor()

# Crie uma nova tabela
cursor.execute('''
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT
    )
''')

# Insira alguns dados na tabela
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ('João', 'joao@email.com'))
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ('Maria', 'maria@email.com'))

# Salve as alterações
conexao.commit()

# Feche a conexão
conexao.close()
