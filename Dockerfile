FROM python:3.9-slim

WORKDIR /Employee_Management

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app/main.py \
    FLASK_ENV=development

VOLUME ["/Employee_Management/.env"]

CMD ["python", "app/main.py"]
