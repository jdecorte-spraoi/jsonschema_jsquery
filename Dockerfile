FROM python:3.8.2

WORKDIR /app

COPY . /app/.

RUN pip install /app/.

CMD [ "jsquery", "tests/test_schema.json", "Age" ]
