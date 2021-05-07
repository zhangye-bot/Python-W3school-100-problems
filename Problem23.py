"""题目：打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *
   """

list_pattern = []
for i in range(4):
	eg = {
	'space':3-i,
	'star': 2*(i+1)-1
	}
	list_pattern.append(eg)
for j in range(3):
	eg = {
	'space': j+1,
	'star': 2*(2-j)+1
	}
	list_pattern.append(eg)



for item in list_pattern:
	print(' '*item['space'],end='')
	print('*'*item['star'])



