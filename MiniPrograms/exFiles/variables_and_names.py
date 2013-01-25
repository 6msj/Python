cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available." #prints out the value of car which is 100
print "There are only", drivers, "drivers available." #prints out the value of driver which is 30
print "There will be", cars_not_driven, "empty cars today." #prints out the value of cars not driven
print "We can transport", carpool_capacity, "people today." #prints out carpool capacity value
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

