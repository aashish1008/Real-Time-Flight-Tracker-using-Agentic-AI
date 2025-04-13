FROM python:3.10.16
COPY . /app
WORKDIR /app
COPY .env /app/
RUN pip install -r requirements.txt
CMD ["python", "main.py"]