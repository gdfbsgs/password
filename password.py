correct_login = "12345678"
correct_password = "12345678"
login = input("enter login")
password = input("Введите пароль: ")
if password == correct_password and login == correct_login:
    print("logged in")
elif password != correct_password or login != correct_login:
    print("Wrong login or password")
elif password == correct_password and login == correct_login:
    print("Something went wrong")

while True:
    pass