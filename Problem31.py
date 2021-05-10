"""题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday"""

letter_1 = input("Please input the first letter for the day: ")
if letter_1 == 'M':
	print('Monday')
elif letter_1 == 'W':
	print('Wednesday')
elif letter_1 == 'F':
	print('Friday')
elif letter_1 == 'T':
	letter_2 = input("Please input the second letter for the day: ")
	if letter_2 == 'U':
		print('Tuesday')
	else:
		print('Thursday')
else:
	letter_2 = input("Please input the second letter for the day: ")
	if letter_2 == 'A':
		print('Saturday')
	else:
		print('Sunday')
