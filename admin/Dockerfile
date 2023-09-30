FROM python:3.11

ENV PYTHONUNBUFFERED 1
# allows output of the application (e.g. Django logs) to be seen in real-time
# ensure that the Python output is sent straight to the terminal without being first buffered, 
# which allows for real-time viewing of the application output 
# and prevents partial output from being lost in case of a crash.

WORKDIR /app
# create /app folder

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./django_admin /app/
# copy all the files in the current directory to /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]