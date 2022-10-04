from flask import Flask, jsonify
from api_functions.import_functions import get_car_by_license_plate

# define the Flask application
app = Flask(__name__)

# add the first route
@app.route('/')
def index():
    return "Hello world"


@app.route('/show_car')
def show_car():
    car = get_car_by_license_plate("RD799K")
    car_dict = car.to_dict()
    return jsonify(car_dict)

# run the application
if __name__ == '__main__':
    app.run()
