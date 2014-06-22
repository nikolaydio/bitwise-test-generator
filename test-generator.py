import sys
import creator
from mako.template import Template
from xhtml2pdf import pisa             # import python module
import shutil
import getopt
import StringIO
import os


def writePDF(html, fn, folder):
	fn += ".pdf"

	out_f = open("chunk.pdf", "w")
	pisa.showLogging()
	pisaStatus = pisa.CreatePDF(src=html, dest=out_f)

	out_f.close()
	shutil.move("chunk.pdf", fn)

	return pisaStatus.err

def generateHTML(test, template):
	temp = Template(filename=template)
	out = temp.render_unicode(entries=test.entries,variant=test.number)

	return out

def writeHTML(html, fn):
	fn += ".html"

	text_f = open(fn, "w")
	text_f.write(html.encode('utf_16'))
	text_f.close()

import argparse
def main():
	def boolean_value(string):
		if(string == "True" or string == "true"):
			return True
		elif(string == "False" or string == "false"):
			return False
		raise argparse.ArgumentTypeError("Should be true or false.")
	def number_range(start, end):
		def test(string):
			num = int(string)
			if num >= start and num <= end:
				return num
			else:
				raise argparse.ArgumentTypeError("Should be between " + start + " and " + end)
		return test

	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-c','--count',
		help="number of tests to generate",
		type=number_range(1, 10000), default=1)
	parser.add_argument('-d','--difficulty', help= 
		"Between 1 and 100", type=number_range(1, 100), default=40)
	parser.add_argument('-o','--output_dir', help=
		"Output directory", default="./tests/")
	parser.add_argument('-gp','--gen-pdf', help='Generate PDFs',
		type=boolean_value, default=True)
	parser.add_argument('-p','--prefix', help="Test filename prefix",
		default="test")
	parser.add_argument('-t','--template', help="Text template to use",
		default="templates/default.html")
	args = parser.parse_args()

	try:
		os.makedirs(args.output_dir)
	except OSError:
		pass

	test_list = []
	for i in range(args.count):
		test = creator.compose_test(args.difficulty)
		test.number = i + 1
		filename = args.output_dir + "/" + args.prefix + str(i+1)

		html = generateHTML(test, args.template)
		writeHTML(html, filename)
		if args.gen_pdf:
			writePDF(html, filename, "./")

		test_list.append(test)

	filename = args.output_dir + "/testAnswers"
	temp = Template(filename='templates/answerSheet.html')
	html = temp.render_unicode(variants=test_list)
	writeHTML(html, filename)
	if args.gen_pdf:
		writePDF(html, filename, "./")
	


if __name__ == "__main__":
	main()