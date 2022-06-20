FROM python:3.9

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install -r requirements.txt
RUN pip3 install requests

ENV SECRET_KEY=""
ENV DATABASE_NAME=""
ENV DATABASE_USER=""
ENV DATABASE_PASSWORD=""
ENV DATABASE_HOST=""
ENV DATABASE_PORT=3306

CMD docker rmi $(docker images -f "dangling=true" | grep "<none>.*<none>" | awk '{ print $3; }')

ADD run.sh /code
RUN chmod +x run.sh


RUN mkdir /evaluacion
ADD servidor.py /evaluacion
ADD mensajes.py /evaluacion
ADD cliente.py /evaluacion


RUN mkdir /app
WORKDIR /app

RUN mkdir /bd_archivos

RUN mktemp -d /evaluacion/EvalScript-XXXXX

RUN useradd usuario1 -s /bin/bash
RUN useradd usuario2 -s /bin/bash


RUN chown -R usuario1 /code
RUN chmod -R 500 /code
RUN chown -R usuario1 /app


RUN chown -R usuario2 /evaluacion
RUN chmod -R 777 /evaluacion


RUN chown -R usuario2 /bd_archivos
RUN chmod -R 777 /bd_archivos

CMD /bin/bash -c '/code/run.sh'
