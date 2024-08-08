# ParkingMeter.py

print("What's crackin' dude, this here's a parking meter!")
park_time = 4
print("park_time time is ", park_time, " hours.")

rate = 4
cost = 0
if park_time > 3:
    cost = rate *3
    # Drop the rate by $2
    rate -= 2
    # Get the remainder of the parking time
    park_time -= 3
    # Add to the current cost
    cost += rate * park_time
    print("The cost of parking in this fabled spot is $", cost)
else:
    cost = rate * park_time
    print ("The cost of parking in this fabled spot is $", cost)