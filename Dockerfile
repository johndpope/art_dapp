FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y \
    python \
    python-dev \
    python-distribute \
    python-pip \
    npm

RUN pip3 install -r requirements.txt \
    npm install -g npm \
    npm install \
    npm i truffle \
