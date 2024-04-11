import click


result=(1,2,3,4,5,6,7,8,9)	
lines = 0
for x in result:
	print(x)
	lines = lines+1
	if lines == 2:
		print("-- Quit (q) --")
		next = click.getchar()   # Gets a single character
		lines = 0
		if next == "q":
			break
		else:
			continue
			


'''
print('Continue? [yn] ')
c = click.getchar()   # Gets a single character


if c == 'y':
    print('We will go on')
elif c == 'n':
    print('Abort!')
else:
    print('Invalid input :(')
'''