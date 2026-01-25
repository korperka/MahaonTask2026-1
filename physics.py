def get_distance(func):
    def wrapper(initial_speed, end_speed, time):
        acceleration = func(initial_speed, end_speed, time)
        distance = initial_speed*time + (acceleration*time**2)/2
        print(distance)

    return wrapper

@get_distance
def get_acceleration(initial_speed, end_speed, time):
    acceleration = (end_speed-initial_speed)/time
    print(acceleration)
    return acceleration

try:
    get_acceleration(int(input("Введите начальную скорость")), int(input("Введите конечную скорость")), int(input("Введите время")))
except ValueError:
    print("Данные должны быть числом")
except ZeroDivisionError:
    print("Время не может быть нулевым")