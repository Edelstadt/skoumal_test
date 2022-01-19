FROM python:3.10

ENV PYTHDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /skoumal_test

COPY Pipfile Pipfile.lock /skoumal_test/
RUN pip install pipenv && pipenv install --system

COPY . /skoumal_test/

RUN chmod +x ./skoumal_test/manage.py
