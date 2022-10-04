from flask import Flask, jsonify, render_template, request
from api_functions.import_functions import get_car_by_license_plate

# define the Flask application
app = Flask(__name__)

# add the first route
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/show_car', methods=['GET', 'POST'])
def show_car():
    if request.method == 'POST':
        selected_plate = request.form.get('plate')
        car = get_car_by_license_plate(selected_plate, as_dict=True)
        selected_car = car[0]
        return render_template("show_car.html",
                           selected_car=selected_car)
    else:
        return render_template("show_car.html")

# run the application
if __name__ == '__main__':
    app.run()
