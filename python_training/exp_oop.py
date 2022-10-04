from cars.cars import Car


if __name__ == '__main__':
    my_car = Car('OPEL', 'KADET')
    my_car_2 = Car('TESLA', 'MODEL 3')
    my_car_3 = Car('TOYOTA', 'YARIS')

    my_car_2.reserve()

    cars_list = [my_car, my_car_2, my_car_3]
    reserved_cars_list = []

    for car in cars_list:
        if car.availability == 'reserved':
            reserved_cars_list.append(car)

    pass