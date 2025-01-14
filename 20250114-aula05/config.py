import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeBase

# Cria variáveis de ambiente a partir dos valores no arquivo .env
load_dotenv()

# A função create_engine cria o motor de conexão ao banco
# O parâmetro echo define se os comandos SQL correspondentes serão exibidos ou não no terminal
engine = create_engine(url=os.getenv("DATABASE_URL"), echo=True)

# Agora criamos a sessão de acesso ao banco, que utilizará a conexão que foi criada
session = scoped_session(sessionmaker(bind=engine, autoflush=False))

# Criar a classe base que representa o mapeamento entre classes e tabelas no banco de dados
class Base(DeclarativeBase):
    pass
