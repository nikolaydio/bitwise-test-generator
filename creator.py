import random

sym = {}
sym[0] = 1
sym[1] = 2
sym[2] = 2
sym[3] = 3
sym[4] = 2
sym[5] = 4
sym[6] = 3
sym[7] = 3
sym[8] = 2
sym[9] = 4
sym[10] = 4
sym[11] = 5
sym[12] = 5
sym[13] = 5
sym[14] = 3
sym[15] = 1

def new_hex(bits, diff):
	return random.randrange(0, 2 ** bits)

class Entry():
	def __init__(self):
		self.answer = []
	def __str__(self):
		s = "Entry -> "
		s += "\nAnswer: " + str(self.answer)
		return s

class OrQuestion(Entry):
	def __init__(self, diff):
		self.orig = new_hex(16, diff)
		self.mask = new_hex(4, diff)
		self.shift = new_hex(4, diff)

		self.answer = (self.orig | (self.mask << self.shift))
	def format(self):
		s = ""
		s += "int orig = " + hex(self.orig)
		s += "\nint insert = " + hex(self.mask)
		s += "\nint a = orig | (insert << " + str(self.shift) + ")"
		return s
class AndQuestion(Entry):
	def __init__(self, diff):
		self.orig = new_hex(16, diff)
		self.mask = new_hex(4, diff)
		self.shifta = new_hex(4, diff)
		self.shiftb = new_hex(4, diff)

		a = self.orig | (self.mask << self.shifta)
		b = self.orig | (self.mask << self.shiftb)
		self.answer = a & b

	def format(self):
		s = ""
		s += "int orig = " + hex(self.orig)
		s += "\nint insert = " + hex(self.mask)
		s += "\nint a = orig | (insert << " + str(self.shifta) + ")"
		s += "\nint b = orig | (insert << " + str(self.shiftb) + ")"
		s += "\nint AND = a & b"
		return s

class XorQuestion(Entry):
	def __init__(self, diff):
		self.orig = new_hex(16, diff)
		self.mask = new_hex(4, diff)
		self.shifta = new_hex(4, diff)
		self.shiftb = new_hex(4, diff)

		a = self.orig | (self.mask << self.shifta)
		b = self.orig | (self.mask << self.shiftb)
		self.answer = a ^ b

	def format(self):
		s = ""
		s += "int orig = " + hex(self.orig)
		s += "\nint insert = " + hex(self.mask)
		s += "\nint a = orig | (insert << " + str(self.shifta) + ")"
		s += "\nint b = orig | (insert << " + str(self.shiftb) + ")"
		s += "\nint XOR = a ^ b"
		return s



class Test():
	def __init__(self, diff):
		self.entries = []
		self.diff = diff

	def add(self, entry):
		self.entries.append(entry)
	def __str__(self):
		s = ""
		for i in self.entries:
			s += str(i) + "\n"
		return s

def compose_test(diff):
	test = Test(diff)

	for i in range(2):
		test.add(OrQuestion(diff))
	for i in range(2):
		test.add(AndQuestion(diff))

	for i in range(1):
		test.add(XorQuestion(diff))
	return test
	#entries.append(new_and_question())
	#entries.append(new_and_question())

	#entries.append(new_xor_question())
	#entries.append(new_shift_question())

	#entries.append(new_shift_and_xor_question())
	#entries.append(new_shift_and_xor_dec_question())

	#entries.append(new_basic_if())
	#entries.append(new_adv_if())