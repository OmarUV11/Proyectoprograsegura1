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

ADD run.sh /code
RUN chmod +x run.sh

RUN mkdir /app
WORKDIR /app

CMD /bin/bash -c '/code/run.sh'
