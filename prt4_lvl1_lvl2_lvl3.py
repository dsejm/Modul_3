import json

def create_file(person_data):
    with open("personal_data.json", "w") as file:
        json.dump(person_data, file)


def user_operation(login, password):
    print("вход или регистрация? ")
    while True:
        uns1 = input().lower()
        if uns1 == "вход":
            login_function(login, password)
        elif uns1 == "регистрация":
            register(login, password)
        else:
            print("Некорретный ввод! Введите вход или регистрация")


def register(login, password):
    with open("personal_data.json", "r", encoding="utf=8") as file:
        person_data = json.load(file)
        login = input("Введите ваш логин: ").lower()
        if login in person_data.keys():
            print("Пользователь с таким логином уже зарегистрирован!\nЖелаете выполнить вход?(да\нет)")
            while True:
                uns2 = input().lower()
                if uns2 == "да":
                    login_function(login, password)
                elif uns2 == "нет":
                    break
                else:
                    print("Некорретный ввод! Введите да или нет")

        else:
            with open("personal_data.json", "w", encoding="utf=8") as file:
                password = input("Введите ваш пароль: ").lower()
                person_data[login] = password
                json.dump(person_data, file)
            print("Пользователь успешно зарегистрирован! Желаете выполнить вход? (да\нет)")
            uns3 = input().lower()
            while True:
                if uns3 == "да":
                    login_function(login, password)
                elif uns3 == "нет":
                    break
                else:
                    print("Некорретный ввод! Введите да или нет")

def login_function(login, password):
    with open("personal_data.json", "r", encoding="utf=8") as file:
        person_data = json.load(file)
        login = input("Введите ваш логин: ").lower()
        if login not in person_data.keys():
            print("Пользователь с таким логином еще не зарегистрирован!\nЖелаете выполнить регистрацию?(да\нет)")
            while True:
                uns2 = input().lower()
                if uns2 == "да":
                    register(login, password)
                elif uns2 == "нет":
                    break
                else:
                    print("Некорретный ввод! Введите да или нет")
        elif login in person_data.keys():
            password = input("Введите ваш пароль: ").lower()
            while True:
                if person_data[login] == password:
                    print("Вход успешно выполнен!")
                    print("Секретная информация для пользователей, выполнивших вход")
                    user_operation(login, password)
                elif person_data[login] != password:
                    print("Неверный пароль! Попробуйте еще раз")
                    login_function(login, password)
                else:
                    print("Упс! Что-то пошло не так. Попробуйте позже")
                    user_operation(login, password)
        # elif login in person_data.keys():
        #     password = input("Введите ваш пароль: ").lower()
        #     for item in person_data:
        #         if login and password in item.items():





person_data = {}
login = ""
password = ""
# create_file() #Для корректной работы функцию следует вызвать только в первый запуск программы. После создания файла следует убрать вызов функции
user_operation(login, password)

