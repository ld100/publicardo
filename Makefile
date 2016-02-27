init:
	pip install -r requirements.txt && cp config/settings.yml.example config/settings.yml

freeze:
	pip freeze > requirements.txt

clean:
	rm destination/* && bin/cleanpyc.sh

process:
	python bin/run.py

autopep:
	autopep8 --in-place --aggressive --aggressive *.py
