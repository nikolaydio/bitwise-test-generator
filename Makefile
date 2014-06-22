build:
	@mkdir -p build
	@rm build -r
	cxfreeze --target-dir=build -c -s test-generator.py
	@mkdir -p build
	@mkdir -p build/font
	@mkdir -p build/templates
	@mkdir -p build/style
	
	cp font build/ -r
	cp templates build/ -r
	cp style build/ -r
	
	zip -r build.zip build/*

web:
	python test-generator.py -c 10 -d 25 -gp false -o /var/www/html/tp/
