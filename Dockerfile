FROM python:3

RUN mkdir -p /home/app

COPY . /home/app

RUN pip3 install --no-cache-dir -r /home/app/requirements.txt

EXPOSE 3000

CMD ["python3", "/home/app/index.py"]

