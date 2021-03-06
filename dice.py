import random # because life is random no mather what...
from pynput import keyboard
import os, time
import sys, termios
import player

humans = int(input('Specify number of human players [1]: ') or 1) # default is one (you)
temp_robots = 0 if humans > 1 else 1
robots = int(input('Specify number of robot players [' + str(temp_robots)  + ']: ') or temp_robots) # default is one (unless you set more humans - then its zero)
names = input('Set player names (separated by space): ').split() # good to know who is who

players = [player.Player(name) for name in names]
cp = players[0]
cp_index = 0

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
		cp.roll = 1
		marker = [False,False,False,False,False]
		print('Saving result to table')
		time.sleep(1.5)
		rollTheDice(nums)
	else:
		cp.roll += 1


def check_game_select():
	termios.tcflush(sys.stdin, termios.TCIFLUSH)
	try:
		cp.game = int(input('Select game from 1 to 15: '))
		if cp.game not in range(1,16):
	                print('\r'+'\x1b[1A'+'\x1b[2K'+'Invalid selection!',end='',flush=True)
	                check_game_select()
		else:
			print('\r'+'\x1b[1A'+'\x1b[2K'+'Game '+str(cp.game)+' selected. Please choose your numbers!',end='',flush=True)
	except ValueError:
		print('\r'+'\x1b[1A'+'\x1b[2K'+'Numeric required!',end='',flush=True)
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
	cp.score = cp.scoreFunc();
	if cp.round == 0: cp.game += 1
	cp_index = 0 if cp_index == len(players) - 1 else cp_index + 1
	cp = players[cp_index] 

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

headrow = '|      |      |'
for name in names:
	headrow += name[:17].center(17) + '|'

np = len(names)


def table():

	sep0 = ' ______________'+np*'__________________'
	sep0 = sep0[:-1] # this will remove the last underscore character
	sep1 = '\n|------|------+'+np*'-----+-----+-----|'
	sep2 = '\n|======+======+'+np*'=====+=====+=====|'
	sep3 = '\n|______|______|'+np*'_________________|'

	print(sep0)
	print(headrow,sep3)
	print('| CODE | GAME |'+np*'((1))|((2))|((3))|',sep2)
	print('|   1  |  1s  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.ones),players)))[1:],sep1)
	print('|   2  |  2s  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.twos),players)))[1:],sep1)
	print('|   3  |  3s  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.threes),players)))[1:],sep1)
	print('|   4  |  4s  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.fours),players)))[1:],sep1)
	print('|   5  |  5s  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.fives),players)))[1:],sep1)
	print('|   6  |  6s  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.sixes),players)))[1:],sep1)
	print('|      | -50  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.total1),players)))[1:],sep2)
	print('|   7  |  2k  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.double),players)))[1:],sep1)
	print('|   8  |  3k  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.triple),players)))[1:],sep1)
	print('|   9  |  2+2 |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.doubles),players)))[1:],sep1)
	print('|  10  |  3+2 |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.full),players)))[1:],sep1)
	print('|  11  |  1-5 |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.straight),players)))[1:],sep1)
	print('|  12  |  2-6 |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.straight2),players)))[1:],sep1)
	print('|  13  |  4k  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.quatro),players)))[1:],sep1)
	print('|  14  |  5k  |',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.general),players)))[1:],sep1)
	print('|  15  |CHANCE|',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.chance),players)))[1:],sep2)
	print('|      | TOTAL|',''.join(list(map(lambda x:'{0:^5}|{1:^5}|{2:^5}|'.format(*x.total2),players)))[1:],sep2)
	print('|      | SCORE|',''.join(list(map(lambda x:(str(x.score)).center(17) + '|',players)))[1:],sep3)

rollTheDice(nums)

while True:
	with keyboard.Listener(on_release=on_release) as listener:
		listener.join()
	break

