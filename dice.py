import random # because life is random no mather what...
from pynput import keyboard
import os

marker = [False,False,False,False,False] # these are selected dice
nums = [random.randint(1,6) for i in range(5)]

def rollTheDice(numbers):
	global marker
	global nums
	nums = [numbers[i] if marker[i] else random.randint(1,6) for i in range(5)]
	numstr = ' '.join(str(number) for number in nums)
	os.system('clear')
	table()	
	print(numstr,'Current player:',current_player.name.upper(),'Roll :',current_player.roll)
	
	print(markerLine(marker),end='',flush=True)
	current_player.roll += 1
	if current_player.roll > 3:
		writeResult()
		current_player.game += 1
		current_player.roll = 1
		marker = [False,False,False,False,False]

def writeResult():
	if   current_player.game == 1: current_player.ones[current_player.round]   = 1*(nums.count(1) - 3) 
	elif current_player.game == 2: current_player.twos[current_player.round]   = 2*(nums.count(2) - 3) 
	elif current_player.game == 3: current_player.threes[current_player.round] = 3*(nums.count(3) - 3) 
	elif current_player.game == 4: current_player.fours[current_player.round]  = 4*(nums.count(4) - 3) 
	elif current_player.game == 5: current_player.fives[current_player.round]  = 5*(nums.count(5) - 3) 
	elif current_player.game == 6: current_player.sixes[current_player.round]  = 6*(nums.count(6) - 3) 
	print(current_player.ones,current_player.twos,current_player.threes,current_player.fours,current_player.fives,current_player.sixes)

# define on_release method from pyinput module to track keys 0 to 5 and ESC
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
	if key == keyboard.KeyCode(char = '0'):
		rollTheDice(nums)
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
temp_robots = 0 if humans > 1 else 1
robots = int(input('Specify number of robot players [' + str(temp_robots)  + ']: ') or temp_robots) # default is one (unless you set more humans - then its zero)
names = input('Set player names (separated by space): ').split() # good to know who is who
print(names)

headrow = '|      |'
for name in names:
	headrow += name[:17].center(17) + '|'

np = len(names)
dice = 5


class Player:
	def __init__(self,name):
		self.name = name
		self.round = 0
		self.game = 1
		self.roll = 1
		self.ones = ['-','-','-']
		self.twos = ['-','-','-']
		self.threes = ['-','-','-']
		self.fours = ['-','-','-']
		self.fives = ['-','-','-']
		self.sixes = ['-','-','-']
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


players = [Player(name) for name in names]
current_player = players[0]
print(players[0],current_player)

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
	print('|  2s  |',''.join(list(map(lambda x:(str(x.twos[0])).center(5) + '|' + (str(x.twos[1])).center(5) + '|' + (str(x.twos[2])).center(5) + '|',players)))[1:],sep1)
	print('|  3s  |',''.join(list(map(lambda x:(str(x.threes[0])).center(5) + '|' + (str(x.threes[1])).center(5) + '|' + (str(x.threes[2])).center(5) + '|',players)))[1:],sep1)
	print('|  4s  |',''.join(list(map(lambda x:(str(x.fours[0])).center(5) + '|' + (str(x.fours[1])).center(5) + '|' + (str(x.fours[2])).center(5) + '|',players)))[1:],sep1)
	print('|  5s  |',''.join(list(map(lambda x:(str(x.fives[0])).center(5) + '|' + (str(x.fives[1])).center(5) + '|' + (str(x.fives[2])).center(5) + '|',players)))[1:],sep1)
	print('|  6s  |',''.join(list(map(lambda x:(str(x.sixes[0])).center(5) + '|' + (str(x.sixes[1])).center(5) + '|' + (str(x.sixes[2])).center(5) + '|',players)))[1:],sep1)
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

rollTheDice(nums)

while True:
	with keyboard.Listener(on_release=on_release) as listener:
		listener.join()
	break

