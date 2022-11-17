FROM python:3.9-buster

WORKDIR /home/
COPY ./requirements.txt /home/requirements.txt

# Add CLI tools
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl wget ftp tree p7zip-full 
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN useradd -ms /bin/bash newuser
# copy credentials files
COPY ./credentials /home/newuser/.basedosdados/credentials
COPY ./templates /home/newuser/.basedosdados/templates
COPY ./config.toml /home/newuser/.basedosdados/config.toml
# copy code files
COPY ./utils.py /home/newuser/utils.py
COPY ./script.py /home/newuser/script.py
COPY ./download.sh /home/newuser/download.sh
# change owner of credentials and templates
RUN chown -R newuser:newuser /home/newuser/.basedosdados
RUN chown -R newuser:newuser /home/newuser/
USER newuser
WORKDIR /home/newuser
ENV GOOGLE_APPLICATION_CREDENTIALS=/home/newuser/.basedosdados/credentials/staging.json
# ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["python", "script.py", "microdados_movimentacao","202101"]