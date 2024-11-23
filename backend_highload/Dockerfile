# Dockerfile

# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы из текущей директории на хосте в директорию /app контейнера
COPY . /app/

# Устанавливаем зависимости из requirements.txt
RUN pip install -r requirements.txt

# Выполняем миграции базы данных
RUN python manage.py migrate

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
