FROM python:latest

WORKDIR /river_compass

COPY ./requirements.txt /river_compass
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /river_compass
