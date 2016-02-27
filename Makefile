init:
	pip install -r requirements.txt && cp config/settings.yml.example config/settings.yml

freeze:
	pip freeze > requirements.txt

clean:
	bin/cleanpyc.sh && rm destination/*

process:
	bin/publicardo

autopep:
	autopep8 --in-place --aggressive --aggressive lib/*.py
