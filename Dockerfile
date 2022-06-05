FROM python:3.8

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install -r requirements.txt

RUN pip3 install requests

ADD pruebas/ /code

RUN pip3 install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8000
