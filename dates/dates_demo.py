import pytz
from datetime import datetime, date, timedelta
#  no installation required as datetime is builtin package

# current date and time

now = datetime.now()
print(now)

# current date
now = date.today()
print(now)

# custom date
doj = datetime(2023,12,25,10,30,0)
print(doj)

# format the dat and time display
now = datetime.now()
format_date = now.strftime("%Y/%B/%d %H:%M:%S")
format_date = now.strftime("%Y/%B/%d")
print(format_date)

# Format Code	Description	Example
# %Y	Year (4 digits)	    2023
# %m	Month (01 to 12)	03
# %d	Day of the month	09
# %H	Hour (00 to 23)	    15
# %M	Minute (00 to 59)	45
# %S	Second (00 to 59)	30
# %A	Full weekday name	Monday
# %B	Full month name	    October

# parsing dates from strings
dob = "1989-10-25"
print(type(dob))
parse_date = datetime.strptime(dob,"%Y-%m-%d")
print(parse_date)
print(type(parse_date))

# date arithmetic
print(now)
ten_days_after = now + timedelta(days=10)
ten_days_before = now - timedelta(days=10)
print(ten_days_after)
print(ten_days_before)
one_week_after = now + timedelta(weeks = 1)
one_week_before = now - timedelta(weeks = 1)
print(one_week_after)
print(one_week_before)


# extract components of date
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# working with time zones
# install a libreary called pytz
# tz = pytz.timezone("America/New_York")
# tz = pytz.timezone("Asia/Singapore")
tz = pytz.timezone("Asia/Kolkata")
time_in_ny = datetime.now(tz)
print(time_in_ny)