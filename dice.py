import random # because life is random no mather what...
from pynput import keyboard
import os, time
import sys, termios

marker = [False,False,False,False,False] # these are selected dice
nums = [random.randint(1,6) for i in range(5)] #random set of 5 dice

def rollTheDice(numbers):
	global marker
	global nums
	nums = [numbers[i] if marker[i] else random.randint(1,6) for i in range(5)]
	numstr = ' '.join(str(number) for number in nums)
	os.system('clear')
	print('Current player:',cp.name.upper(),'Round:',cp.round+1,'Game:',cp.game,'Roll:',cp.roll)
	table()	
	print(numstr)
	
	print(markerLine(marker),end='',flush=True)
	if cp.round == 1 and cp.roll == 1:
		check_game_select()
		cp.roll += 1
	elif cp.roll == 3:
		if cp.round == 2:
			check_game_select()
		writeResult()
		if cp.round == 0: cp.game += 1
		cp.roll = 1
		marker = [False,False,False,False,False]
		print('Saving result to table')
		time.sleep(1.5)
		rollTheDice(nums)
	else:
		cp.roll += 1


def check_game_select():
	termios.tcflush(sys.stdin, termios.TCIFLUSH)
	cp.game = int(input('Select game from 1 to 15: '))
	if cp.game < 1 or cp.game > 15:
		print('Invalid game number!',end='',flush=True)
		check_game_select()


def writeResult():
	global cp, cp_index
	if   cp.game == 1: cp.ones[cp.round]      = 1*(nums.count(1) - 3); cp.total1[cp.round] = cp.total1f();  
	elif cp.game == 2: cp.twos[cp.round]      = 2*(nums.count(2) - 3); cp.total1[cp.round] = cp.total1f();  
	elif cp.game == 3: cp.threes[cp.round]    = 3*(nums.count(3) - 3); cp.total1[cp.round] = cp.total1f();
	elif cp.game == 4: cp.fours[cp.round]     = 4*(nums.count(4) - 3); cp.total1[cp.round] = cp.total1f(); 
	elif cp.game == 5: cp.fives[cp.round]     = 5*(nums.count(5) - 3); cp.total1[cp.round] = cp.total1f(); 
	elif cp.game == 6: cp.sixes[cp.round]     = 6*(nums.count(6) - 3); cp.total1[cp.round] = cp.total1f(); 
	elif cp.game == 7: cp.double[cp.round]    = double();    cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	elif cp.game == 8: cp.triple[cp.round]    = triple();    cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	elif cp.game == 9: cp.doubles[cp.round]   = doubles();   cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	elif cp.game ==10: cp.full[cp.round]      = full();      cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	elif cp.game ==11: cp.straight[cp.round]  = straight();  cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	elif cp.game ==12: cp.straight2[cp.round] = straight2(); cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	elif cp.game ==13: cp.quatro[cp.round]    = quatro();    cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	elif cp.game ==14: cp.general[cp.round]   = general();   cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	elif cp.game ==15: cp.chance[cp.round]    = sum(nums);   cp.total2[cp.round] = cp.total2f(); cp.round = cp.change_round();
	cp_index = 0 if cp_index == len(players) - 1 else cp_index + 1
	cp = players[cp_index] 
#	print(cp.ones,cp.twos,cp.threes,cp.fours,cp.fives,cp.sixes)

def double():
	result = [2*i for i in range(1,7) if nums.count(i) > 1]
	return max(result) if result else 0

def triple():
	result = [3*i for i in range(1,7) if nums.count(i) > 2]
	return result[0] if result else 0

def doubles():
	doubles = [2*i for i in range(1,7) if nums.count(i) > 1]
	if len(doubles) == 2: 
		return sum(doubles)
	else: 
		return sum([4*i for i in range(1,7) if nums.count(i) > 3])

def full():
	double = [2*i for i in range(1,7) if nums.count(i) == 2]
	triple = [3*i for i in range(1,7) if nums.count(i) == 3]
	return double[0] + triple[0] if double and triple else sum([5*i for i in range(1,7) if nums.count(i) == 5])

def straight():
	return 15 if 1 in nums and 2 in nums and 3 in nums and 4 in nums and 5 in nums else 0

def straight2():
	return 20 if 2 in nums and 3 in nums and 4 in nums and 5 in nums and 6 in nums else 0

def quatro():
	return sum([4*i for i in range(1,7) if nums.count(i) > 3])

def general():
	return sum([5*i+50 for i in range(1,7) if nums.count(i) == 5])


# define on_release method from pyinput module to track keys 0 to 5 and ESC
# update marker list and call function markerLine
def on_release(key):
#	print('{0} released'.format(key))
	if key == keyboard.KeyCode(char = 'z'):
		marker[0] = not(marker[0])
		print(markerLine(marker),end='',flush=True)
		#print(markerLine(marker))
	if key == keyboard.KeyCode(char = 'x'):
		marker[1] = not(marker[1])
		print(markerLine(marker),end='',flush=True)
	if key == keyboard.KeyCode(char = 'c'):
		marker[2] = not(marker[2])
		print(markerLine(marker),end='',flush=True)
	if key == keyboard.KeyCode(char = 'v'):
		marker[3] = not(marker[3])
		print(markerLine(marker),end='',flush=True)
	if key == keyboard.KeyCode(char = 'b'):
		marker[4] = not(marker[4])
		print(markerLine(marker),end='',flush=True)
	if key == keyboard.Key.space:
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

headrow = '|      |      |'
for name in names:
	headrow += name[:17].center(17) + '|'

np = len(names)


class Player:
	def __init__(self,name):
		self.name = name
		self.round = 1
		self.game = 1
		self.roll = 1
		self.ones = ['-','-','-']
		self.twos = ['-','-','-']
		self.threes = ['-','-','-']
		self.fours = ['-','-','-']
		self.fives = ['-','-','-']
		self.sixes = ['-','-','-']
		self.total1 = ['-','-','-']
		self.double = ['-','-','-']
		self.triple = ['-','-','-']
		self.doubles = ['-','-','-']
		self.full = ['-','-','-']
		self.straight = ['-','-','-']
		self.straight2 = ['-','-','-']
		self.quatro = ['-','-','-']
		self.general = ['-','-','-']
		self.chance = ['-','-','-']
		self.total2 = ['-','-','-']
		self.score = '-'

	def total1f(self):
		if  type(self.ones[self.round])   is int \
		and type(self.twos[self.round])   is int \
		and type(self.threes[self.round]) is int \
		and type(self.fours[self.round])  is int \
		and type(self.fives[self.round])  is int \
		and type(self.sixes[self.round])  is int:
			sum = self.ones[self.round] + self.twos[self.round] + self.threes[self.round] + self.fours[self.round] + self.fives[self.round] + self.sixes[self.round]
			if sum < 0:
				return sum - 50
			else:
				return sum
		else:
			return '-'
		
	def total2f(self):
		if  type(self.total1[self.round])    is int \
		and type(self.double[self.round])    is int \
		and type(self.triple[self.round])    is int \
		and type(self.doubles[self.round])   is int \
		and type(self.full[self.round])      is int \
		and type(self.straight[self.round])  is int \
		and type(self.straight2[self.round]) is int \
		and type(self.quatro[self.round])    is int \
		and type(self.general[self.round])   is int \
		and type(self.chance[self.round])    is int:
			total = self.total1[self.round]    + \
                                self.double[self.round]    + \
                                self.triple[self.round]    + \
                                self.doubles[self.round]   + \
                                self.full[self.round]      + \
                                self.straight[self.round]  + \
                                self.straight2[self.round] + \
                                self.quatro[self.round]    + \
                                self.general[self.round]   + \
                                self.chance[self.round]
			return total
		else:
			return '-'

	def change_round(self):
		if type(self.total2[self.round]) is int:
			return self.round + 1  
		else:
			return self.round

players = [Player(name) for name in names]
cp = players[0]
cp_index = 0
#print(players[0],cp)

def table():

	sep0 = ' ______________'+np*'__________________'
	sep0 = sep0[:-1] # this will remove the last underscore character
	sep1 = '\n|------|------+'+np*'-----+-----+-----|'
	sep2 = '\n|======+======+'+np*'=====+=====+=====|'
	sep3 = '\n|______|______|'+np*'_________________|'

	print(sep0)
	print(headrow,sep3)
	print('| CODE | GAME |'+np*'((1))|((2))|((3))|',sep2)
	print('|   1  |  1s  |',''.join(list(map(lambda x:(str(x.ones[0])).center(5) + '|' + (str(x.ones[1])).center(5) + '|' + (str(x.ones[2])).center(5) + '|',players)))[1:],sep1)
	print('|   2  |  2s  |',''.join(list(map(lambda x:(str(x.twos[0])).center(5) + '|' + (str(x.twos[1])).center(5) + '|' + (str(x.twos[2])).center(5) + '|',players)))[1:],sep1)
	print('|   3  |  3s  |',''.join(list(map(lambda x:(str(x.threes[0])).center(5) + '|' + (str(x.threes[1])).center(5) + '|' + (str(x.threes[2])).center(5) + '|',players)))[1:],sep1)
	print('|   4  |  4s  |',''.join(list(map(lambda x:(str(x.fours[0])).center(5) + '|' + (str(x.fours[1])).center(5) + '|' + (str(x.fours[2])).center(5) + '|',players)))[1:],sep1)
	print('|   5  |  5s  |',''.join(list(map(lambda x:(str(x.fives[0])).center(5) + '|' + (str(x.fives[1])).center(5) + '|' + (str(x.fives[2])).center(5) + '|',players)))[1:],sep1)
	print('|   6  |  6s  |',''.join(list(map(lambda x:(str(x.sixes[0])).center(5) + '|' + (str(x.sixes[1])).center(5) + '|' + (str(x.sixes[2])).center(5) + '|',players)))[1:],sep2)
	print('|      | -50  |',''.join(list(map(lambda x:(str(x.total1[0])).center(5) + '|' + (str(x.total1[1])).center(5) + '|' + (str(x.total1[2])).center(5) + '|',players)))[1:],sep2)
	print('|   7  |  2k  |',''.join(list(map(lambda x:(str(x.double[0])).center(5) + '|' + (str(x.double[1])).center(5) + '|' + (str(x.double[2])).center(5) + '|',players)))[1:],sep1)
	print('|   8  |  3k  |',''.join(list(map(lambda x:(str(x.triple[0])).center(5) + '|' + (str(x.triple[1])).center(5) + '|' + (str(x.triple[2])).center(5) + '|',players)))[1:],sep1)
	print('|   9  |  2+2 |',''.join(list(map(lambda x:(str(x.doubles[0])).center(5) + '|' + (str(x.doubles[1])).center(5) + '|' + (str(x.doubles[2])).center(5) + '|',players)))[1:],sep1)
	print('|  10  |  3+2 |',''.join(list(map(lambda x:(str(x.full[0])).center(5) + '|' + (str(x.full[1])).center(5) + '|' + (str(x.full[2])).center(5) + '|',players)))[1:],sep1)
	print('|  11  |  1-5 |',''.join(list(map(lambda x:(str(x.straight[0])).center(5) + '|' + (str(x.straight[1])).center(5) + '|' + (str(x.straight[2])).center(5) + '|',players)))[1:],sep1)
	print('|  12  |  2-6 |',''.join(list(map(lambda x:(str(x.straight2[0])).center(5) + '|' + (str(x.straight2[1])).center(5) + '|' + (str(x.straight2[2])).center(5) + '|',players)))[1:],sep1)
	print('|  13  |  4k  |',''.join(list(map(lambda x:(str(x.quatro[0])).center(5) + '|' + (str(x.quatro[1])).center(5) + '|' + (str(x.quatro[2])).center(5) + '|',players)))[1:],sep1)
	print('|  14  |  5k  |',''.join(list(map(lambda x:(str(x.general[0])).center(5) + '|' + (str(x.general[1])).center(5) + '|' + (str(x.general[2])).center(5) + '|',players)))[1:],sep1)
	print('|  15  |CHANCE|',''.join(list(map(lambda x:(str(x.chance[0])).center(5) + '|' + (str(x.chance[1])).center(5) + '|' + (str(x.chance[2])).center(5) + '|',players)))[1:],sep2)
	print('|      | TOTAL|',''.join(list(map(lambda x:(str(x.total2[0])).center(5) + '|' + (str(x.total2[1])).center(5) + '|' + (str(x.total2[2])).center(5) + '|',players)))[1:],sep2)
	print('|      | SCORE|'+np*(17*' '+'|'),sep3)

rollTheDice(nums)

while True:
	with keyboard.Listener(on_release=on_release) as listener:
		listener.join()
	break

