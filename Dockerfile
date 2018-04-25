FROM python:2.7
RUN apt-get update && apt-get -y install supervisor
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]
