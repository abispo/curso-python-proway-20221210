from config import session
from messages import USER_MENU
from models import User, Profile

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
                pass

            case 2:
                _add_user()