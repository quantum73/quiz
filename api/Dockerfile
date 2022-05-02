FROM python:3.8-alpine

ENV API_HOME=/home/api
RUN mkdir $API_HOME
WORKDIR $API_HOME
ADD . $API_HOME

RUN pip3 install -U pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x /home/api/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/home/api/entrypoint.sh"]
