# this program is not supported in notepad++ use online compiler

# to print current datetime
import datetime as dt

current_datetime= dt.datetime.today()
print("current_datetime: ",current_datetime)
current_date= dt.date.today()
print("current_date: ",current_date)
current_time= dt.datetime.now()
print("current_time: ",current_time)

print("year: ",current_datetime.year)
print("month: ",current_datetime.month)
print("day: ",current_datetime.day)
print("hour: ",current_datetime.hour)
print("minute: ",current_datetime.minute)
print("second: ",current_datetime.second)

print("----------------------------------------------")

# to print custom datetime
cus_datetime= dt.datetime(2022,12,1,10,11,30,8377)
print("cus_datetime: ", cus_datetime)
cus_date= dt.date(2022,12,1)
print("cus_date: ", cus_date)
cus_time= dt.time(12,12,12,124)
print("cus_time: ",cus_time)

print("----------------------------------------------")

cus_datetime= dt.datetime(2022,12,1,10,11,30,8377)
print("cus_datetime: ", cus_datetime)

print("year: ",cus_datetime.year)
print("month: ",cus_datetime.month)
print("day: ",cus_datetime.day)
print("hour: ",cus_datetime.hour)
print("minute: ",cus_datetime.minute)
print("second: ",cus_datetime.second)

print("----------------------------------------------")
#to find difference between two dates
date1= dt.date(2022,2,11)
ny=dt.date(2023,1,1)
difference= ny-date1
print(difference)

print("----------------------------------------------")
#to find difference between current date and customed dates
date2= dt.datetime.now()
ny=dt.datetime(2023,1,1)
difference1= ny-date2
print(difference1)

import datetime as dt

current=dt.datetime.now()
print(current)

print("--------------------------------")
#to change the format

cformat= current.strftime("%a" "%A"  ) # %a = short form of day# %A = full form of day
cformat1= current.strftime( "%b"  "%B" )# %b = short form of month# %B = full form of month
cformat2= current.strftime( "%y" "%Y") # %y = short form of year# %Y = full form of year
cformat3= current.strftime( "%M" "%S")# %M -minutes //%S -seconds
cformat4= current.strftime( "%H" "%I")# %H- hours(24hr) // %I- hour(12hr)
cformat5= current.strftime( "%j")# find serial no of day of the year
print(cformat)
print(cformat1)
print(cformat2)
print(cformat3)
print(cformat4)
print(cformat5)