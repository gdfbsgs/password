time=int(input("Введите время: "))
if time <= 17 and time >= 13:
    print("Посылку получить можно")
elif time >= 9 and time <= 11:
    print("Посылку получить можно")
elif time == 12:
    print("Посылку получить нельзя")
elif time >= 18 or time <= 8:
    print("Посылку получить нельзя")



