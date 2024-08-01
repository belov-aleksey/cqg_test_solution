.PHONY: run

PYTHON = python3
SCRIPT = main.py
ARGS = config.txt text.txt

replace:
	$(PYTHON) $(SCRIPT) $(ARGS)