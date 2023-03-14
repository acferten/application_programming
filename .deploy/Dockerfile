FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR usr/src/app

COPY ../requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY .. /usr/src/app
#RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
