import datetime 

# Create the date time object
current_datetime = datetime.datetime.now()
# Adding 3 days to a datetime object
new_datetime = current_datetime + datetime.timedelta(weeks=2)
# Output the formated datetime 
print("Now datetime:", current_datetime)
print("Update datetime:", new_datetime)

# You can compare datetime objects to determine their relative order.
# if new_datetime > current_datetime:
#     print("The specified datetime is in the future.")
