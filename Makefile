all:
	python3 src/generate.py > output/gen.md
	cd output && ../node_modules/cleaver/bin/cleaver gen.md
