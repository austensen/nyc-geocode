FROM nycplanning/docker-geosupport:latest

COPY requirements.txt .
RUN pip install --upgrade pip && \
  pip install -r requirements.txt

COPY . /nyc-geocode
WORKDIR /nyc-geocode

ENTRYPOINT ["python3", "geocode.py"]

ENV PYTHONBUFFERED 1
