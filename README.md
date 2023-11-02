# App

Этот проект представляет собой приложение, реализованное с использованием FastAPI. Он также включает в себя контейнер PostgreSQL для хранения данных.

## Запуск проекта

Проект запускается с использованием Docker Compose, что позволяет легко настроить окружение для разработки и развертывания. Перед запуском убедитесь, что Docker и Docker Compose установлены на вашем компьютере.

**1. Склонируйте репозиторий:**

```bash
    git clone https://github.com/AnCapitan/App.git
```

**2. Создайте файл .env для настройки переменных окружения. Пример:**

*.env*
```bash
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    POSTGRES_NAME=имя_бд
    POSTGRES_USER=имя_юзера
    POSTGRES_PASSWORD=пароль_юзера
    BINANCE_API_KEY=ваш_ключ_апи_binance
    BINANCE_SECRET_KEY=ваш_секретный_ключ_binance
```

**3. Запустите проект с помощью Docker Compose:**

```bash
docker-compose up --build
```

4. Приложение FastAPI будет доступно по адресу http://0.0.0.0:5000. Вы можете использовать Swagger UI для взаимодействия с API, перейдя по адресу http://0.0.0.0:5000/docs.