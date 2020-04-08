country = input('Where are you from? ')
age = input('Your age: ')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
    	print('You can have a driving license.')
    else:
    	print('You cannot have a driving license.')