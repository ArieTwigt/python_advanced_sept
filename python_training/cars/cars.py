from cars.garage import Garage


class Car(Garage):

    # initial parameters of the class
    def __init__(self, brand: str,
                       model: str, 
                       color: str,
                       price: float=0.0,
                       id: int=None,
                       purpose: str="transport",
                       availability: str="available"):
                       
        self.brand = brand
        self.model = model
        self.color = color 
        self.id = id
        self.price = price
        self.purpose = purpose
        self.availability = availability
        

    # method for displaying the car
    def display(self):
        print(f"This is a {self.brand} of {self.model}")


    # method for specifying the price of the car
    def set_price(self, price: float):
        self.price = price
        print(f"setting the price to {price}")

    
    # method for increasing or decreasing the price of the car
    def change_price(self, change_amount: float):
        current_price = self.price
        self.price += change_amount
        print(f"The price changed from {current_price} to {self.price} (change of {change_amount})")


    # def add id to the car
    def add_car_id(self, id):
        self.id = id

    # represent the clas in a formatted way
    def __repr__(self):
        return repr(f"{self.brand} - {self.model} : {self.availability}")


if __name__ == "__main__":
    print("THis comes from Cars")