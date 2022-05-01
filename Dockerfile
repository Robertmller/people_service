FROM python:3.8.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT python3 manage.py runserver 0.0.0.0:80 && python3 manage.py makemigrations && python3 manage.py migrate

EXPOSE 80

