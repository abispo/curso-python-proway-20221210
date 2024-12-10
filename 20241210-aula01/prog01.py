"""
Python com Banco de Dados

Trabalhando com SQLite3

Assim como em outras linguagens, podemos utilizar o Python para acessar bancos de dados. Geralmente precisamos de uma biblioteca (conector) para acessar esses bancos. No caso do SQLite3, já vem suportado na biblioteca padrão do Python.
"""

import os
import sqlite3

if __name__ == "__main__":
    """
    Geralmente, seguimos os seguintes passos para executar comandos no banco de dados através do Python
    1. Importamos a biblioteca (conector) de acesso ao banco de dados
    2. Definimos uma connection string, que nada mais é do que uma string que contém as informações necessárias para acessar o banco de dados (usuario, senha, servidor, etc)
    3. Criamos uma conexão com o banco de dados utilizando a connection string definida
    4. Criamos um cursor a partir da conexão que foi criada. É pelo cursor que vamos enviar os comandos SQL para o banco de dados.
    5. Definimos os comandos SQL como strings, e mandamos o cursor executar.
    6. Se necessário, pegamos o resultado do comando sql que foi executado.
    7. Fechamos a conexão com o banco de dados
    """

    # 2. Aqui criamos a connection string de acesso. No caso do SQLite3, como o banco de dados é um arquivo, a connection string será o caminho completo do arquivo.
    connection_string = os.path.join(os.getcwd(), "db.sqlite3")

    # 3. Criar a conexão com o banco de dados
    connection = sqlite3.connect(connection_string)

    # 4. Criar o cursor que será utilizado para executar os comandos SQL
    cursor = connection.cursor()
