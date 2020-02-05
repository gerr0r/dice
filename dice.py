import random # because life is random no mather what...
from pynput import keyboard


marker = [False,False,False,False,False] # these are selected dice

def rollTheDice():
	print(marker)

# define on_release method from pyinput module to track keys 1 to 5 and ESC
# update marker list and call function markerLine
def on_release(key):
#	print('{0} released'.format(key))
	if key == keyboard.KeyCode(char = '1'):
		marker[0] = not(marker[0])
		print(markerLine(marker),end='',flush=True)
		#print(markerLine(marker))
	if key == keyboard.KeyCode(char = '2'):
		marker[1] = not(marker[1])
		print(markerLine(marker),end='',flush=True)
	if key == keyboard.KeyCode(char = '3'):
		marker[2] = not(marker[2])
		print(markerLine(marker),end='',flush=True)
	if key == keyboard.KeyCode(char = '4'):
		marker[3] = not(marker[3])
		print(markerLine(marker),end='',flush=True)
	if key == keyboard.KeyCode(char = '5'):
		marker[4] = not(marker[4])
		print(markerLine(marker),end='',flush=True)
	if key == keyboard.Key.enter:
		rollTheDice()
	if key == keyboard.Key.esc:
		return False

# this function will return ^-marks with selected dice
def markerLine(arr):
	string = ''
	for i in range(5):
		if arr[i]:
			string += '^ '
		else:
			string += '  '
		#print(string)
	return "\r"+string+"\x1b[K"

humans = int(input('Specify number of human players [1]: ') or 1) # default is one (you)
print(humans)
if humans > 1:
	temp_robots = 0
else:
	temp_robots = 1 
robots = int(input('Specify number of robot players [' + str(temp_robots)  + ']: ') or temp_robots) # default is one (unless you set more humans - then its zero)
print(robots)
names = input('Set player names (separated by space): ').split() # good to know who is who
print(names)

headrow = '|      |'
for name in names:
	headrow += name[:17].center(17) + '|'

np = len(names)
dice = 5
#print(type(dice))
def pluralize(num):
	if num == 1:
		return 'die'
	else:
		return 'dice'

#print(dice,pluralize(dice),'rollin...')


class Player:
	def __init__(self):
		self.ones = ['-','-','-']
		self.twos = -6
		self.threes = -9
		self.fours = -12
		self.fives = -15
		self.sixes = -18
		self.total1 = -50
		self.double = 0
		self.triple = 0
		self.doubles = 0
		self.full = 0
		self.straight = 0
		self.straight2 = 0
		self.quatro = 0
		self.general = 0
		self.sum = 0
		self.total2 = 0
		self.score = 0


players = [Player() for name in names]
#print(players[0].ones)

def table():

	sep0 = '\n _______'+np*'__________________'
	sep0 = sep0[:-1] # this will remove the last underscore character
	sep1 = '\n|------+'+np*'-----+-----+-----|'
	sep2 = '\n|======+'+np*'=====+=====+=====|'
	sep3 = '\n|______|'+np*'_________________|'

	print(sep0)
	print(headrow,sep3)
	print('| GAME |'+np*'((1))|((2))|((3))|',sep2)
	print('|  1s  |',''.join(list(map(lambda x:(str(x.ones[0])).center(5) + '|' + (str(x.ones[1])).center(5) + '|' + (str(x.ones[2])).center(5) + '|',players)))[1:],sep1)
	print('|  2s  |'+np*'     |     |     |',sep1)
	print('|  3s  |'+np*'     |     |     |',sep1)
	print('|  4s  |'+np*'     |     |     |',sep1)
	print('|  5s  |'+np*'     |     |     |',sep1)
	print('|  6s  |'+np*'     |     |     |',sep2)
	print('| -50  |'+np*'     |     |     |',sep2)
	print('|  2k  |'+np*'     |     |     |',sep1)
	print('|  3k  |'+np*'     |     |     |',sep1)
	print('|  2+2 |'+np*'     |     |     |',sep1)
	print('|  3+2 |'+np*'     |     |     |',sep1)
	print('|  1-5 |'+np*'     |     |     |',sep1)
	print('|  2-6 |'+np*'     |     |     |',sep1)
	print('|  4k  |'+np*'     |     |     |',sep1)
	print('|  5k  |'+np*'     |     |     |',sep1)
	print('|  SUM |'+np*'     |     |     |',sep2)
	print('| TOTAL|'+np*'     |     |     |',sep2)
	print('| SCORE|'+np*'                 |',sep3)

table()

numbers = [random.randint(1,6) for i in range(dice)]
print(' '.join(str(number) for number in numbers))

while True:
	with keyboard.Listener(on_release=on_release) as listener:
		listener.join()
	break

