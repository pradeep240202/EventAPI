FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD python manage.py migrate && python create_users.py && python manage.py runserver 0.0.0.0:8000
