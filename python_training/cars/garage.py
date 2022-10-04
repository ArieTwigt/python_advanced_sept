class Garage:


    # initial parameters
    def __init__(self, garage_name):
        self.garage_name = garage_name

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

    pass