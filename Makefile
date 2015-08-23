all:
	python3 src/generate.py > gen.md
	node_modules/cleaver/bin/cleaver gen.md
