#Defining the variables. Note that the '=' does not mean 'equals'. It means that you are assigning a value to a variable.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#Using the variables in mathematical calculations
cars_not_driven = cars - drivers
cars_driven = drivers
#Note in the line below that there are always spaces around operators for ease of reading.
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


#After using the variables in calculations, they have values. These values are outputted to the console:
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
