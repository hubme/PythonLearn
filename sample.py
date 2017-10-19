class Fibs:
	def __init__(self):
		self.a = 0;
		self.b = 1;
	def next(self):
		self.a. self.b = self.b, self.a + self.b;
	def __iter__(self):
		return self;

fibs = Fibs();

for f in Fibs():
	if f > 5:
		print f;
		break;