FROM python:3.7

EXPOSE 9000
RUN pip3 install flask

RUN mkdir /app
COPY app.py /app/
WORKDIR /app

ENTRYPOINT ["python3", "server.py"]