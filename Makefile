# Makefile for Real-Time Pair Programming App

# --- Backend Commands ---
backend-venv:
	python3 -m venv backend/venv

activate-backend:
	@echo "Run: source backend/venv/bin/activate"

install-backend:
	pip install -r backend/requirements.txt

run-backend:
	python3 backend/app/main.py

# --- Frontend Commands ---
install-frontend:
	cd frontend && npm install

run-frontend:
	cd frontend && npm start

# --- Full Setup ---
setup:
	python3 -m venv backend/venv
	@echo "Activate venv manually, then run: make install-backend"

run:
	@echo "Starting backend and frontend..."
	@echo "Open two terminals:"
	@echo "Terminal 1: make run-backend"
	@echo "Terminal 2: make run-frontend"
