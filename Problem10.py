#暂停一秒输出，并格式化当前时间。

from datetime import date
from datetime import datetime
import time

today = date.today()
print("Today's date: ",today)
while True:
	now = datetime.now()
	print("Time now: ",now)
	time.sleep(1)