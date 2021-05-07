#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
int_series = input("请输入三个整数:")
int_series_float = int_series.split(' ')
try:
	int_1 = int(int_series_float[0])
	int_2 = int(int_series_float[1])
	int_3 = int(int_series_float[2])
	list_int = [int_1,int_2,int_3]
	list_int.sort()
	print(list_int)
except FormatError:
	print("输入格式有误")
