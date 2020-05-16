.PHONY: all clean uninstall install test dist sdist twine

all:
	@grep -Ee '^[a-z].*:' Makefile | cut -d: -f1 | grep -vF all

clean:
	rm -rf build/ dist/ *.egg-info/ *.c *.so *.h __pycache__

uninstall: clean
	@echo pip uninstalling exif_delete
	$(shell pip uninstall -y exif_delete >/dev/null 2>/dev/null)
	$(shell pip uninstall -y exif_delete >/dev/null 2>/dev/null)
	$(shell pip uninstall -y exif_delete >/dev/null 2>/dev/null)

install: uninstall
	python setup.py install

test:
	python test/test_*.py

dist: install
	python setup.py sdist

sdist: dist

twine: dist
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

