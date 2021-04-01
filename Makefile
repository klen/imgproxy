VIRTUAL_ENV ?= env

all: $(VIRTUAL_ENV)

$(VIRTUAL_ENV): setup.cfg
	@[ -d $(VIRTUAL_ENV) ] || python -m venv $(VIRTUAL_ENV)
	@$(VIRTUAL_ENV)/bin/pip install -e .[tests,build]
	@touch $(VIRTUAL_ENV)

.PHONY: t test
# target: test - Run tests
t test: $(VIRTUAL_ENV)
	@$(VIRTUAL_ENV)/bin/py.test tests.py

.PHONY: mypy
mypy: $(VIRTUAL_ENV)
	@$(VIRTUAL_ENV)/bin/mypy imgproxy.py
