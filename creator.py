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
		self.input = []
		self.answer = []
	def __str__(self):
		s = "Input: "
		for i in self.input:
			s += str(i) + "  "
		s += "\nAnswer: " + str(self.answer)
		return s

class OrQuestion(Entry):
	def __init__(self, diff):
		orig = new_hex(16, diff)
		mask = new_hex(4, diff)
		shift = new_hex(4, diff)

		self.input = (orig, mask, shift)
		self.answer = (orig | (mask << shift))


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

	test.add(OrQuestion(diff))
	test.add(OrQuestion(diff))

	return test
	#entries.append(new_and_question())
	#entries.append(new_and_question())

	#entries.append(new_xor_question())
	#entries.append(new_shift_question())

	#entries.append(new_shift_and_xor_question())
	#entries.append(new_shift_and_xor_dec_question())

	#entries.append(new_basic_if())
	#entries.append(new_adv_if())