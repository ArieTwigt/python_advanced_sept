from cars.cars import Car
from cars.garage import Garage


if __name__ == '__main__':
    my_car = Car("NISSAN", "Micra", "RED", 1000, id=1)
    my_car_2 = Car("TOYOTA", "YARIS", "BLUE", 5000, id=2)
    my_car_3 = Car("OPEL", "ASTRA", "WHITE", 3000, id=3)

    # define a garage
    my_garage = Garage("Arie's Garage")

    # add cars to the garage list
    my_garage.add_to_cars_list(my_car, my_car_2, my_car_3)

    # show the ids of the car
    my_garage.show_cars_list_by_id()

    pass