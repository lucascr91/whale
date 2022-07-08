# Pull official base image
FROM python:3.9-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set working directory and copy python scripts
RUN mkdir /scripts
WORKDIR /scripts
COPY *.py ./

CMD ["python", "create_table.py"]
