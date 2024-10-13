from Car import Car

BMW = Car('BMW', 300, 'Black', 2.8)
Audi = Car('Audi', 280, 'White', 3.5)
Mercedes = Car('Mercedes', 260, 'Blue', 4)
#BMW.sound()
#print('It boost from 0 to 100 km/h for', BMW.boost)
#BMW.long_sound()
#print('It can drive for about', BMW.max_speed, 'km/h')

list_cars = [BMW, Audi, Mercedes]
for index in range(len(list_cars)):
    print(list_cars[index].color)
    list_cars[index].sound()
for car in list_cars:
    print(car.color)
    car.sound()

