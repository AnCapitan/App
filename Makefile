DC = docker-compose
BACKEND_FILE = docker/backend.yaml
STORAGE_FILE = docker/storage.yaml
FRONTEND_FILE = docker/frontend.yaml

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} up --build -d

.PHONY: drop-storage
drop-storage:
	${DC} -f ${STORAGE_FILE} down

.PHONY: backend
backend:
	${DC} -f ${BACKEND_FILE} up --build -d

.PHONY: drop-backend
drop-backend:
	${DC} -f ${BACKEND_FILE} down

.PHONY: frontend
backend:
	${DC} -f ${FRONTEND_FILE} up --build -d

.PHONY: drop-frontend
drop-backend:
	${DC} -f ${FRONTEND_FILE} down

.PHONY: all
all:
	${DC} -f ${STORAGE_FILE} -f ${BACKEND_FILE} -f ${FRONTEND_FILE} up --build -d

.PHONY: drop-all
drop-all:
	${DC} -f ${STORAGE_FILE} -f ${BACKEND_FILE} -f ${FRONTEND_FILE} down

.PHONY: logs
logs:
	${DC} -f ${STORAGE_FILE} -f ${BACKEND_FILE} -f ${FRONTEND_FILE} logs -f

