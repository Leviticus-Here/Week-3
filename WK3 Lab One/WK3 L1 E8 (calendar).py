# Inport the 'calender' module
import calendar

# Prompt the user to input the year and month
y = int(input("The year is: "))
m = int(input("The month is: "))

# Print the calendar for the specified year and month
print(calendar.month(y, m))