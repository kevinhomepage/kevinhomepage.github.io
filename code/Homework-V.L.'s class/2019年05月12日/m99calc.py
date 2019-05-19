def run():
	for i in range(9):
		printlist = []
		for j in range(i + 1):
			printlist.append(str(i + 1) + "x" + str(j + 1) + "=" + str(( i + 1 ) * ( j+ 1 )) + " ")
		print(printlist)

run()