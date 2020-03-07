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
		try:
			total = self.ones[self.round] + self.twos[self.round] + self.threes[self.round] + self.fours[self.round] + self.fives[self.round] + self.sixes[self.round]
			return total - 50 if total < 0 else total
		except:
			return '-'


	def total2f(self):
		try:
			return self.total1[self.round]    + \
                               self.double[self.round]    + \
                               self.triple[self.round]    + \
                               self.doubles[self.round]   + \
                               self.full[self.round]      + \
                               self.straight[self.round]  + \
                               self.straight2[self.round] + \
                               self.quatro[self.round]    + \
                               self.general[self.round]   + \
                               self.chance[self.round]
		except:
			return '-'


	def scoreFunc(self):
		try:
			return sum(self.total2)
		except:
			return '-'


	def change_round(self):
		return self.round + 1 if type(self.total2[self.round]) is int else self.round
