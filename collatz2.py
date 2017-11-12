def collatz(number):
	if number % 2 == 0:
		return number // 2
	elif number % 2 == 1:
		return 3 * number + 1

try:
	print('Enter number:')
	inputNumber = int(input())
	while True:
		print(collatz(inputNumber)) # 调用函数后，print()才可打印返回值
		inputNumber = collatz(inputNumber) # 关键！
		if inputNumber == 1:
			break
except ValueError:
	print('Please enter a integer.')
