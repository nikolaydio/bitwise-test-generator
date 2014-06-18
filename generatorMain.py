import sys
import creator
from mako.template import Template

def print_help():
	_help = """python3 test-generator.py <number of tests> <difficuly> <optional parameters>

Number of tests -> number of variantes
Difficulty -> between 1(easiest) to 100(hardest)
Optional paramters ->
	-prefix \t Variant filename prefix
	-answer-prefix \t Prefix to prepend to the files that contain the answers
	-folder \t Folder to generate files into
	-genpdf \t Should we generate pdfs? (No by default)
	-genhtml \t SHould we generate htmls? (Yes by default)
	"""
	print(_help)
def main():
	if len(sys.argv) < 3:
		print("Not enough arguments.")
		print_help()
		exit(-1)
	test_count = 1
	output_dir = "./tests"
	for i in range(test_count):
		test = creator.compose_test(5)
		#output the test
		temp = Template(filename='template.html')
		out = temp.render_unicode(entries=test.entries)

		text_f = open("out.html", "w")
		text_f.write(out.encode('utf_16'))
		text_f.close()
	


if __name__ == "__main__":
	main()