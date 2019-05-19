little_one = 0
big_one = 0
run = True
def mon():
	if (little_one / 3 * 1) + (big_one * 3) == 100:
		print(little_one,big_one)

while run:
	little_one += 3
	mon()
	little_one -= 3
	big_one += 1
	mon()
	little_one += 3
	mon()
	if big_one == 100:
		run = False
