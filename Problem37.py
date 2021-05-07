print('请输入10个数字: ')

i = 0
number_list = []
while i < 10:
	number = int(input("输入一个数字: "))
	number_list.append(number)
	i = i + 1

for i in range(0,len(number_list)):
	print(number_list[i])


print('排列之后:')
number_list.sort()

for i in range(0,len(number_list)):
	print(number_list[i])