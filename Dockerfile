FROM python:slim

WORKDIR /home/githubusers

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY scripts scripts
COPY main.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP main.py
ENV FLASK_ENV production


CMD ["./boot.sh"]