import random

min = input('請輸入最小值: ')
max = input('請輸入最大值: ')
min = int(min)
max = int(max)

ans = random.randint(min, max)
count = 0

while True:
	count += 1
	num = input("猜一個介於最小值與最大值之間數字:")
	num = int(num)
	if num == ans:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > ans:
		print('比答案大')
	else:
		print('比答案小')
	
	print('這是你猜的第', count, '次')

