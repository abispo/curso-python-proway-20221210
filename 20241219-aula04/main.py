from config import engine
from messages import MAIN_MENU
from models import *

if __name__ == "__main__":
    # O método create_all cria todas as tabelas que ainda não foram criadas no banco de dados
    Base.metadata.create_all(engine)

    while True:
        print(MAIN_MENU)
        option = int(input("Informe a opção escolhida: "))

        match option:
            case 0:
                print("SAINDO...")
                break

            case 1:
                pass