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


<<<<<<< HEAD


=======
>>>>>>> 7cbeb95148eb72086a3f01c4d0b2885a6adbe8f1
RUN mkdir /evaluacion
ADD servidor.py /evaluacion 
ADD mensajes.py /evaluacion



#RUN mktemp -d -t EvalScript-XXXXX
RUN mkdir /app
WORKDIR /app

RUN useradd usuario1 -s /bin/bash
RUN useradd usuario2 -s /bin/bash


#codigo valito
#RUN useradd -u 0 -o -g 0 usuario2 -s /bin/bash


RUN chown -R usuario1 /code
RUN chmod -R 500 /code
RUN chown -R usuario1 /app



RUN chown -R usuario2 /evaluacion
RUN chmod -R 766 /evaluacion
<<<<<<< HEAD
RUN usermod -a -G 0 usuario2
RUN mktemp -d -t EvalScript-XXXXX || RUN chown -R usuario2 /EvalScript-XXXXX




CMD python3 '/evaluacion/servidor.py'
=======
RUN mktemp -d /evaluacion/EvalScript-XXXXX 
RUN chown -R usuario2 /evaluacion 
#|| RUN chgrp -R 1001 /tmp/EvalScript-XXXXX
>>>>>>> 7cbeb95148eb72086a3f01c4d0b2885a6adbe8f1

CMD python3 '/evaluacion/servidor.py'


#USER dueño

CMD /bin/bash -c '/code/run.sh'

