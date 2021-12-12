FROM python:3.8-buster
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN /usr/local/bin/python -m pip install flask uWSGI
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
RUN apt-get update
RUN adduser myuser
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
CMD ["uwsgi", "app/app.ini"]