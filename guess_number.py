import random

r = random.randint(1, 100)
while True:
	num = input('請猜數字：')
	num = int(num) #casting型別轉換
	if num == r:
		print('恭喜答對！')
		break
	elif num > r:
		print('太大囉！')
	elif num < r:
		print('太小囉！')