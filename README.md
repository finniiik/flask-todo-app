# Список задач на Flask

Простое веб приложение для ведения списка дел: добавление, изменение, отметка о выполнении и удаление задач. Данные хранятся в SQLite.

## Запуск локально

```
pip install -r requirements.txt
python run.py
```

Приложение откроется по адресу http://localhost:5000

## Запуск в Docker

```
docker build -t flask-todo .
docker run -p 5000:5000 flask-todo
```

Готовый образ собирается автоматически при каждом пуше:

```
docker run -p 5000:5000 ghcr.io/finniiik/flask-todo-app:latest
```
