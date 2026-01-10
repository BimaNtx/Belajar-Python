import datetime
import time
import calendar

from datetime import date, time, datetime

# Object tanggal dan waktu
d = date(2025, 10, 7)
print("Date:", d)

t = time(14, 30, 15)
print(f'time: {t}')

dt = datetime(2025, 10, 7, 14, 30, 15)
print(f"Datetime: {dt}")

now = datetime.now()
print(f"Sekarang: {now}")

# !format tanggal & waktu
from datetime import datetime, timedelta

date_string = "2020, 10, 7, 13:23:11"
dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed  datetime:", dt)