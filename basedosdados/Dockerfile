FROM python:3.9-buster

WORKDIR /home
COPY ./requirements.txt /home/requirements.txt

# RUN apt update && apt add bash && apk add --no-cache make && apk add g++
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN useradd -ms /bin/bash newuser
COPY ./script.py /home/script.py
COPY ./credentials /home/newuser/.basedosdados/credentials
COPY ./templates /home/newuser/.basedosdados/templates
COPY ./config.toml /home/newuser/.basedosdados/config.toml
# change owner of credentials and templates
RUN chown -R newuser:newuser /home/newuser/.basedosdados
USER newuser
ENV GOOGLE_APPLICATION_CREDENTIALS=/home/newuser/.basedosdados/credentials/staging.json
ENTRYPOINT ["tail", "-f", "/dev/null"]
# CMD ["python", "script.py"]