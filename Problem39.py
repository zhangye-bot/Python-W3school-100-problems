#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。


list = [4, 5, 10, 17, 18, 20, 30]



def insert_num(number):
	index = 0 
	i = 0
	while i < len(list):
		if list[i] < number:
			i = i + 1
		else:
			break
	
	list.insert(i,number)
	return list

print(insert_num(8))