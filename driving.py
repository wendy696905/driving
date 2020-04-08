country = input('Where are you from? ')
age = input('Your age: ')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
    	print('You can have a driving license.')
    else:
    	print('You cannot have a driving license.')
elif country == 'America':
    if age >= 16:
    	print('You can have a driving license.')
    else:
    	print('You cannot have a driving license.')
else:
	print('this can only track the country of Taiwan or America')