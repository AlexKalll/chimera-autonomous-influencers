setup:
	pip install -r requirements.txt

test:
	docker build -t chimera-autonomous-influencers:local .
	docker run --rm chimera-autonomous-influencers:local

test-local:
	pytest tests/

spec-check:
	python scripts/verify_specs.py
