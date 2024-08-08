from datetime import datetime

# now() method is used to
# get object containing
# current date and time.
now_method = datetime.now()

# strftime() method used to
# create a string representing
# the current time.
currenttime = now_method.strftime("%H:%M:%S")
print("Current Time = "), currenttime