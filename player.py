
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


	def scoreFunc(self):
		try:
			return sum(self.total2)
		except TypeError:
			return '-'


	def change_round(self):
		if type(self.total2[self.round]) is int:
			return self.round + 1  
		else:
			return self.round
