from api_functions.import_functions import calculate_circle

# the input will be a  'str' by default
selected_diameter = input("Enter diameter:\n")

# convert the 'str' variable to a 'float' data type
#selected_diameter_float = float(selected_diameter)

# insert the diameter value to our function
circle_size = calculate_circle(selected_diameter)

# print the result
print(circle_size)