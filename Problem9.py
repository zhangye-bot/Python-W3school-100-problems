"""题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。"""
import time
dic1 = {
	'key':'a',
	'value':'b'
}

print(dic1['key'])
time.sleep(1)
print(dic1['value'])
