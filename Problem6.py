"""题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""

number = int(input('请输入您想要的斐波那契数列个数: '))
list_Fibonacci = []
if number <= 0:
	print("输入数字有误")
elif number == 1:
	list_Fibonacci.append(0)
elif number == 2:
	list_Fibonacci.append(0)
	list_Fibonacci.append(1)

else:
	list_Fibonacci.append(0)
	list_Fibonacci.append(1)
	for i in range(2,number,1):
		number = list_Fibonacci[i-1] + list_Fibonacci[i-2]
		list_Fibonacci.insert(i,number)

print(list_Fibonacci)

