TESTS_PATH?=tests/
AUTOLOAD_PATH?=autoload.php

test:
	@echo "-----> running tests"
	@phpunit --bootstrap $(AUTOLOAD_PATH) $(TESTS_PATH)

.PHONY: test
