VENV=env
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

install: $(VENV)/bin/activate
	$(PIP) install -r requirements.txt
	$(PIP) install pre-commit
	pre-commit install
	pre-commit install --hook-type commit-msg

run: $(VENV)/bin/activate
	$(PYTHON) main.py
