"""题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。"""


def peaches_calculator(n):
	if n == 1:
		return 1
	else:
		return (peaches_calculator(n-1) + 1) * 2

print(peaches_calculator(10))




"""10  1          1
   9   2          3
   8   3         7


   10    1    

"""
