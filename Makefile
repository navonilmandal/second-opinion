.PHONY: help setup dev backend web extension lint test clean seed

help:
	@echo "Available commands:"
	@echo "  setup      - Install dependencies for all packages"
	@echo "  dev        - Start docker-compose and web frontend"
	@echo "  backend    - Start only the backend services in docker"
	@echo "  web        - Start the React frontend locally"
	@echo "  extension  - Build the Chrome extension"
	@echo "  seed       - Run the data seeding script"
	@echo "  clean      - Remove node_modules, build artifacts, and pycache"

setup:
	cd apps/web && npm install
	cd apps/extension && npm install
	cd services/backend && pip install -r requirements.txt

dev:
	docker-compose up -d postgres redis qdrant backend
	cd apps/web && npm run dev

backend:
	docker-compose up --build

web:
	cd apps/web && npm run dev

extension:
	cd apps/extension && npm run build

seed:
	docker-compose exec backend python -m scripts.seed_benchmark
	docker-compose exec backend python -m scripts.seed_documents

clean:
	find . -type d -name "node_modules" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "__pycache__" -exec rm -rf {} +
