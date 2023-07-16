FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app
CMD cd /app/backend && flask run -h 0.0.0.0 -p 5000
