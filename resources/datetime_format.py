import datetime

# Create the date time object
current_datetime = datetime.datetime.now()
# Formating the datetime object to curtine format, check the file
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# Output the formated datetime 
print("Formatted datetime:", formatted_datetime)
