from datetime import datetime as datetime2
import datetime
#1
current_date = datetime2.now()
five_days_ago = current_date - datetime.timedelta(days=80)#days, hours, seconds, weeks       
print("Five days ago from today was:", five_days_ago)
#2
today = datetime2.now()
yesterday = today.replace(day=today.day - 1)
tomorrow = today.replace(day=today.day + 1)
print("Yesterday was:", yesterday)
print("Today is:", today)
print("Tomorrow will be:", tomorrow)
#3
