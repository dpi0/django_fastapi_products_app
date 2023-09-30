FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code
# create a new dir /code

COPY ./requirements.txt /code/requirements.txt
# req.txt is next to Dockerfile, so copy that into /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# install

COPY ./app /code/app
# NOTE: copy ./app to /code/app
# NOTE: req.txt is already inside /code/app

CMD ["python", "app/run.py"]
# NOTE: my current working dir is /code
# IMP: but run.py is inside /app so that's why app/run.py 