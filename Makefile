all:
	python3 src/generate.py main/slides
	cd main && python3 makeslide.py
