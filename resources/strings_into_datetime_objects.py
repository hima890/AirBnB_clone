import datetime 

# Ceate the datetime object 
date_string = "2022-05-12"
# Format the datetime string into datetime object
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
# Output the formated datetime 
print("Formatted datetime:", parsed_date)