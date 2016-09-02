FROM ubuntu

MAINTAINER Danilo Lima <danlima69@gmail.com>

RUN apt-get update
RUN apt-get install -y lsb-release
RUN apt-get update

RUN apt-get install -y tar git curl vim wget dialog net-tools build-essential

RUN apt-get install -y python python-dev python-distribute python-pip

ADD /app /app

RUN pip install -r /app/requirements.txt

EXPOSE 80

WORKDIR /app

CMD python server.py
