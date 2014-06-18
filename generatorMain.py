import sys
import creator
from mako.template import Template
from xhtml2pdf import pisa             # import python module
import shutil

import StringIO

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

def writePDF(html, fn, folder):
	fn += ".pdf"

	out_f = open("chunk.pdf", "w")
	pisa.showLogging()
	pisaStatus = pisa.CreatePDF(src=html, dest=out_f)

	out_f.close()
	shutil.move("chunk.pdf", fn)

	return pisaStatus.err

def generateHTML(test):
	temp = Template(filename='templates/webtemplate.html')
	out = temp.render_unicode(entries=test.entries,variant=test.number)

	return out

def writeHTML(html, fn):
	fn += ".html"

	text_f = open(fn, "w")
	text_f.write(html.encode('utf_16'))
	text_f.close()


def main():
	if len(sys.argv) < 3:
		print("Not enough arguments.")
		print_help()
		exit(-1)
	test_count = 29
	output_dir = "/var/www/html/tp"
	test_list = []
	for i in range(test_count):
		test = creator.compose_test(5)
		test.number = i + 1
		filename = output_dir + "/test" + str(i+1)

		html = generateHTML(test)
		writeHTML(html, filename)
		writePDF(html, filename, "./")

		test_list.append(test)

	filename = output_dir + "/testAnswers.html"
	temp = Template(filename='templates/answerSheet.html')
	out = temp.render_unicode(variants=test_list)
	text_f = open(filename, "w")
	text_f.write(out.encode('utf_16'))
	text_f.close()
	


if __name__ == "__main__":
	main()