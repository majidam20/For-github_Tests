FROM python:3.7.3

RUN mkdir /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install pandas
RUN pip install PyMySQL

RUN pip install --no-cache-dir -r requirements.txt

COPY people.csv ./
COPY places.csv ./
COPY example.py ./

