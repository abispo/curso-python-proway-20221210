from messages import USER_MENU

def users_management():
    while True:
        print(USER_MENU)
        option = int(input("Informe a opção escolhida: "))

        match option:
            case 0:
                break