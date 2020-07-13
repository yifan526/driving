country = input('please enter your nationality')
if country != 'China' and country != 'USA':
	print ('error') 
else:
	age = input('please enter your age')
	age = int(age)
	if country == 'China':
		if age >= 18:
			print ('you can drive')
		else:
			print ('you cannot drive')
	elif country == 'USA':
		if age >= 16:
			print ('you can drive')
		else:
			print ('you cannot drive')