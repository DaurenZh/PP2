import datetime
#1
current_date = datetime.now()
five_days_ago = current_date - datetime.timedelta(days=5)
print("Five days ago from today was:", five_days_ago)
#2
today = datetime.now()
yesterday = today.replace(day=today.day - 1)
tomorrow = today.replace(day=today.day + 1)
print("Yesterday was:", yesterday)
print("Today is:", today)
print("Tomorrow will be:", tomorrow)
#3
current_datetime = datetime.now()
current_datetime_without_microseconds = datetime(current_datetime.year, current_datetime.month, current_datetime.day, current_datetime.hour, current_datetime.minute, current_datetime.second)
print("Current datetime without microseconds:", current_datetime_without_microseconds)
#4
date1 = datetime(2024, 1, 20, 12, 30, 15)
date2 = datetime(2024, 1, 25, 10, 45, 30)
difference_in_seconds = (date2 - date1).total_seconds()
print("Difference between date2 and date1 in seconds:", difference_in_seconds)

