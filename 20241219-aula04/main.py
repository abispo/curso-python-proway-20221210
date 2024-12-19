from config import engine
from models import *

if __name__ == "__main__":
    # O método create_all cria todas as tabelas que ainda não foram criadas no banco de dados
    Base.metadata.create_all(engine)