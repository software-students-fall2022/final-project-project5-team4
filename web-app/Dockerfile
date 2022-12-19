FROM --platform=linux/amd64 python:3.7-slim

WORKDIR /web-app

ADD . /web-app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4001

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4001"]
