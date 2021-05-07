"""题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。"""
data_1 = input('请输入您想要复制的列表数据：')
list_1 = list(data_1.split(' '))
list_2 = list_1[:]
print(list_2)
