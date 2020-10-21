import random

r = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	num = input('請猜數字：')
	num = int(num) #casting型別轉換
	if num == r:
		print('恭喜答對！')
		print('您總共猜了', count, '次！')
		break
	elif num > r:
		print('太大囉！')
	elif num < r:
		print('太小囉！')
	print('您已經猜了', count, '次！')