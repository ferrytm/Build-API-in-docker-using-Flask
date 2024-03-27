FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask pymysql pandas 

RUN pip install mysqlclient

EXPOSE 3000

CMD ["python", "song_api.py"]
