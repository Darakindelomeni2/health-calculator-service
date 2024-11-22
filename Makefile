IMAGE_NAME=health-calculator-service
PORT=5000

.PHONY: init run test build clean

init:
	@echo "Installation des dépendances..."
	pip install -r requirements.txt

run:
	@echo "Lancement de l'application Flask..."
	python3 app.py

test:
	@echo "Lancement des tests..."
	python3 -m unittest discover

build:
	@echo "Construction de l'image docker..."
	docker build -t $(IMAGE_NAME) .

clean:
	@echo "Nettoyage..."
	docker rmi $(IMAGE_NAME)
