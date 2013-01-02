SHELL := /bin/bash

test-python3:
	python3 test_careful_requests.py

test-python2:
	python test_careful_requests.py

test: test-python3 test-python2

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	find . -type f -name "*.pyc" -exec rm '{}' \;

install:
	python setup.py install

upload:
	python setup.py sdist upload

