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
	test_count = 29
	output_dir = "/var/www/html/tp"
	test_list = []
	for i in range(test_count):
		filename = output_dir + "/test" + str(i+1) + ".html"
		test = creator.compose_test(5)
		#output the test
		temp = Template(filename='templates/webtemplate.html')
		out = temp.render_unicode(entries=test.entries,variant=i+1)

		text_f = open(filename, "w")
		text_f.write(out.encode('utf_16'))
		text_f.close()

		test.number = i + 1
		test_list.append(test)

	filename = output_dir + "/testAnswers.html"
	temp = Template(filename='templates/answerSheet.html')
	out = temp.render_unicode(variants=test_list)
	text_f = open(filename, "w")
	text_f.write(out.encode('utf_16'))
	text_f.close()
	


if __name__ == "__main__":
	main()