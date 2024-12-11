"""
Python com Banco de Dados

Trabalhando com MySQL utilizando a biblioteca pymysql
"""

import json
import os

import pymysql.cursors

import requests


if __name__ == "__main__":
    
    connection = pymysql.connect(
        user="root",
        password="123456",
        host="127.0.0.1",
        database="modulo02_python",
        cursorclass=pymysql.cursors.DictCursor,      # O cursor será um dicionário
    )

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS tb_opcoes")
    cursor.execute("DROP TABLE IF EXISTS tb_perguntas")

    sql = """
        CREATE TABLE tb_perguntas(
            id INT PRIMARY KEY AUTO_INCREMENT,
            texto VARCHAR(200) NOT NULL
        )
    """
    cursor.execute(sql)

    sql = """
        CREATE TABLE tb_opcoes(
            id INT PRIMARY KEY AUTO_INCREMENT,
            pergunta_id INT NOT NULL,
            texto VARCHAR(100) NOT NULL,
            votos INT NOT NULL DEFAULT 0,
            FOREIGN KEY(pergunta_id) REFERENCES tb_perguntas(id)
        )
    """
    cursor.execute(sql)

    # URL do arquivo de enquetes
    url = "https://raw.githubusercontent.com/abispo/shared-files/refs/heads/main/enquetes.json"

    # Baixar o conteúdo da URL
    response = requests.get(url)

    # Definidos os nomes da pasta e do arquivo
    folder_path = os.path.join(os.getcwd(), "tmp")
    file_path = os.path.join(folder_path, "enquetes.json")

    # Se a pasta não existir, será criada
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    
    # Salvamos o conteúdo pego pelo requests como o arquivo enquetes.json
    with open(file_path, 'w', encoding="utf-8") as json_file:
        json_file.write(response.text)

    # Abrir o arquivo para realizar o processamento
    with open(file_path, 'r', encoding="utf-8") as json_file:

        # questions = json.loads(json_file.read())
        questions = json.load(json_file)

        for question in questions:
            question_text = question.get("pergunta")
            sql = "INSERT INTO tb_perguntas(texto) VALUES (%s);"
            cursor.execute(sql, question_text)

            connection.commit()

