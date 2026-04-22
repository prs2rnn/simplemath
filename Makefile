PHONY: test test-verbose clean


test:
	pytest

test-verbose:
	pytest -v

clean:
	rm -rf __pycache__/
	rm -rf *.pyc
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
