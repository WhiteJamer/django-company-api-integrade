FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y

# Ставим зависимости GDAL, PROJ
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev
RUN pip install -r requirements.txt

COPY ../ /app/
WORKDIR /app