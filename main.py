# How to format datetime or time as AM/PM in Python

from datetime import datetime

# ✅ Format datetime as AM/PM
dt_string = '2024-07-21 04:50 PM'
dt_object = datetime.strptime(dt_string, '%Y-%m-%d %H:%M %p')
print(dt_object)

print(dt_object.strftime('%Y-%m-%d %H:%M %p'))