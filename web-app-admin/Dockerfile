FROM --platform=linux/amd64 python:3.7-slim

WORKDIR /web-app-admin

ADD . /web-app-admin

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5001"]
