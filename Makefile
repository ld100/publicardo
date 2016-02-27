SOURCE_DIR=source
DESTINATION_DIR=destination
CONFIG_FILE=config/settings.yml

default:
	echo 'Welcome to Publicardo. Run `bin/publicardo` to process your photos.'

init: install_dependencies copy_default_config

install_dependencies:
	pip install -r requirements.txt

copy_default_config:
	[[ ! -f $(CONFIG_FILE) ]] && cp config/settings.yml.example $(CONFIG_FILE)

freeze:
	pip freeze > requirements.txt

process:
	bin/publicardo

clean_destination:
	rm $(DESTINATION_DIR)/*

clean_source:
	rm $(SOURCE_DIR)/*

clean_cache:
	bin/cleanpyc.sh

clean: clean_destination clean_cache

autopep:
	autopep8 --in-place --aggressive --aggressive lib/*.py
