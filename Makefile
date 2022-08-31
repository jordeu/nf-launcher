SHELL := /bin/bash
.PHONY: all fusionfs

update_launcher:
	curl -s https://get.nextflow.io > launcher/nextflow

publish: update_launcher
	rm -rf dist/
	python3 setup.py sdist
	twine upload -r pypi dist/nf-launcher-*.tar.gz
