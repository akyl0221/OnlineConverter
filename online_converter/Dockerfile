FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /conv

WORKDIR /conv

ADD . /conv/

RUN pip install -U pipenv
RUN pipenv install --system
RUN pip install -r requirements.txt

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["migrate", "runserver", "0.0.0.0:8000"]