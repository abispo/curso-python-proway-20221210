from sqlalchemy import select

from config import session
from messages import USER_MENU
from models import User, Profile

def _select_users():
    statement = select(User)

    # Utilizando o método all do objeto retornado por scalars(), todos linhas do resultado são retornadas como uma lista de objetos do tipo User. Se não utilizarmos o all, o que será retornado será um objeto do tipo ScalarResult, que vai trazer uma linha do resultado a cada vez que for chamado
    # users = session.scalars(statement).all()
    users = session.scalars(statement)

    for user in users:
        print(f"ID: {user.id}")
        print(f"E-mail: {user.email}")
        print(f"Nome: {user.profile.first_name}")
        print(f"Sobrenome: {user.profile.last_name}")
        print(f"Aniversário: {user.profile.birth_date.strftime("%d/%m/%Y")}")

        print('-'*50)


def _add_user_profile(user_id: int, first_name: str, last_name: str, birth_date: str) -> None:
    profile = Profile(
        id=user_id, first_name=first_name, last_name=last_name, birth_date=birth_date
    )
    session.add(profile)
    session.commit()

def _add_user():
    email = input("Informe o e-mail do usuário: ")
    password = input("Informe a senha do usuário: ")
    first_name = input("Informe o primeiro nome do usuário: ")
    last_name = input("Informe o sobrenome do usuário: ")
    birth_date = input("Informe a data de nascimento do usuário (formato AAAA-MM-DD)")

    user = User(
        email=email,password=password
    )
    session.add(user)
    session.commit()

    _add_user_profile(
        user_id=user.id,
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date
    )


def users_management():
    while True:
        print(USER_MENU)
        option = int(input("Informe a opção escolhida: "))

        match option:
            case 0:
                break

            case 1:
                _select_users()

            case 2:
                _add_user()