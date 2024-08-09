# course_work_7


#Для запуска проекта необходимо:.

* Клонировать репозиторий на компьютер. Создать базу данных в БД «PostgreSQL». Создать и заполнить своими данными файл .env. Необходимые для заполнения переменные окружения находятся в файле .env.sample Установить и подключить виртуальное окружение venv python3 -m venv venv source venv/bin/activate Суперпользователь создается командой python manage.py csu Рассылка запускается командами: redis-server celery -A config worker —loglevel=info celery -A config beat —loglevel=info