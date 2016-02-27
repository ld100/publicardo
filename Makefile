clean:
	rm destination/* && bin/cleanpyc.sh

process:
	python bin/run.py

autopep:
	autopep8 --in-place --aggressive --aggressive *.py
