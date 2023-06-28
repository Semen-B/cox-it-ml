# FROM python:3-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
RUN pip install --upgrade pip
WORKDIR /code
RUN pip install Pillow
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src ./src/
COPY ./src/main.py ./main.py
COPY ./src/app/app.py ./app.py

EXPOSE 8000

CMD ["python", "main.py"]
# CMD ["python", "app.py"]