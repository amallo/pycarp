# Makefile: équivalent des "scripts" package.json pour lancer tests, etc.
# Usage: make test, make test-device, etc.

PYTHONPATH := .
PYTHON := python

.PHONY: test test-device

# Tous les tests du core (exécutables sur macOS sans ESP32)
test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s core -p "test_*.py" -v

# Tests du module device uniquement
test-device:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest core.device.tests.test_init_device_command -v
