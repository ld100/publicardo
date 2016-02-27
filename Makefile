clean:
	rm destination/* && bin/cleanpyc.sh

process:
	python run.py

autopep:
	autopep8 --in-place --aggressive --aggressive *.py
