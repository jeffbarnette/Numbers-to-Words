FROM python:3.8.7-slim-buster
ENV PYTHONUNBUFFERED 1

# copy source and install dependencies
RUN mkdir -p /www/app
RUN mkdir -p /www/app/pip_cache
COPY . /www/app/
WORKDIR /www/app
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /www/app

# start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/www/app/start-server.sh"]