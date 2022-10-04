class Garage:


    # initial parameters
    def __init__(self, garage_name: str, cars_list: list=[]):
        self.garage_name = garage_name
        self.cars_list = cars_list

    # add a method for the service
    def add_service(self):
        self.service = "2 weeks service"


    # method to reserve the car
    def reserve(self):
        print(f"Availability of this car was {self.availability}")
        self.availability = "reserved"
        print(f"Availability of this car is now {self.availability}")


    # method for selling the car
    def sold(self):
        print(f"Availability of this car was {self.availability}")
        self.availability = "sold"
        print(f"Availability of this car is now {self.availability}")


    # define method to add car to the list
    def add_to_cars_list(self, *args):
        for car in args:
            self.cars_list.append(car)

    # define a method that shows all cars by its id
    def show_cars_list_by_id(self):
        for car in self.cars_list:
            print(f"{car.id}: {car}")
