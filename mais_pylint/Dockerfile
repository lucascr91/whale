FROM python:3.9-alpine

WORKDIR home

COPY ./ ./
RUN apk update && apk add bash && apk add --no-cache make && apk add g++
RUN python -m pip install --upgrade pip
RUN python -m pip install pylint
WORKDIR /home/mais/python-package/
RUN python -m pip install -r requirements-dev.txt
WORKDIR /home/mais/
CMD ["pylint", "python-package"]
