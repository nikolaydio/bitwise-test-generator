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

class LeftShiftQuestion(Entry):
	def __init__(self, diff):
		self.orig = new_hex(16, diff)
		self.shift = new_hex(4, diff)
		self.answer = self.orig | (1 << self.shift)
	def format(self):
		s = ""
		s += "int orig = " + hex(self.orig)
		s += "\nint left = orig | (1 << " + str(self.shift) + ")"
		return s

class LongXorQuestion(Entry):
	def __init__(self, diff):
		self.value1 = new_hex(32, diff)
		self.value2 = new_hex(32, diff)
		self.shift1 = new_hex(4, diff)
		self.shift2 = new_hex(4, diff)
		self.answer = (self.value1 << self.shift1) ^ (self.value2 >> self.shift2)
	def format(self):
		s = ""
		s += "\nint value1 = " + hex(self.value1)
		s += "\nint value2 = " + hex(self.value2)
		s += "\nint result = (value1 << " + str(self.shift1) + ") ^ (value2 >> " + str(self.shift2) + ")"
		return s
class XorDecQuestion(Entry):
	def __init__(self, diff):
		self.value1 = new_hex(10, diff)
		self.value2 = new_hex(10, diff)
		self.shift1 = new_hex(4, diff)
		self.shift2 = new_hex(4, diff)
		self.answer = (self.value1 << self.shift1) ^ (self.value2 >> self.shift2)
	def format(self):
		s = ""
		s += "\nint value1 = " + str(self.value1)
		s += "\nint value2 = " + str(self.value2)
		s += "\nint result = (value1 << " + str(self.shift1) + ") ^ (value2 >> " + str(self.shift2) + ")"
		return s

class IfShiftQuestion(Entry):
	def __init__(self, diff):
		self.value1 = new_hex(32, diff)
		self.shift1 = new_hex(4, diff)

		if (self.value1 & ( 1 << self.shift1 )) != 0:
			self.answer = 1
		else:
			self.answer = 2
	def format(self):
		s = "int testValue = " + hex(self.value1)
		s += "\nint a = 0;\n if(testValue & (1 << " + str(self.shift1) + "))"
		s += "\na = 1; \nelse\n a = 2;"
		return s

class IfShiftBitQuestion(Entry):
	def __init__(self, diff):
		self.value1 = new_hex(32, diff)
		self.shift1 = new_hex(4, diff)

		if (self.value1 & self.value1 ^ self.value1 | ( 1 << self.shift1 )) != 0:
			self.answer = 1
		else:
			self.answer = 2
	def format(self):
		s = "int testValue = " + hex(self.value1)
		s += "\nint a = 0;"
		s += "\n if(testValue & testValue & testValue | (1 << " + str(self.shift1) + "))"
		s += "\na = 1; \nelse\n a = 2;"
		return s

class OrDecQuestion(Entry):
	def __init__(self, diff):
		self.value1 = new_hex(10, diff)
		self.value2 = new_hex(10, diff)
		self.shift1 = new_hex(4, diff)
		self.shift2 = new_hex(4, diff)
		self.answer = (self.value1 << self.shift1) | (self.value2 >> self.shift2)
	def format(self):
		s = ""
		s += "\nint value1 = " + str(self.value1)
		s += "\nint value2 = " + str(self.value2)
		s += "\nint result = (value1 << " + str(self.shift1) + ") | (value2 >> " + str(self.shift2) + ")"
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

	m = 1
	for i in range(2 * m):
		test.add(OrQuestion(diff))
	for i in range(2 * m):
		test.add(AndQuestion(diff))

	for i in range(1 * m):
		test.add(XorQuestion(diff))

	for i in range(1 * m):
		test.add(LeftShiftQuestion(diff))

	for i in range(1 * m):
		test.add(LongXorQuestion(diff))

	for i in range(1 * m):
		test.add(XorDecQuestion(diff))

	for i in range(1 * m):
		test.add(IfShiftQuestion(diff))

	for i in range(1 * m):
		test.add(IfShiftBitQuestion(diff))

	for i in range(1 * m):
		test.add(XorDecQuestion(diff))

	for i in range(1 * m):
		test.add(OrDecQuestion(diff))
	return test