from cars.garage import Garage

class Car(Garage):

    # initial parameters of the class
    def __init__(self, brand,
                       model, 
                       purpose="transport",
                       availability="available"):
                       
        self.brand = brand
        self.model = model
        self.purpose = purpose
        self.availability = availability
        

    # method for displaying the car
    def display(self):
        print(f"This is a {self.brand} of {self.model}")


    # represent the clas in a formatted way
    def __repr__(self):
        return repr(f"{self.brand} - {self.model} : {self.availability}")