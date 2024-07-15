FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /desafio

COPY . .

RUN pip install boto3 pandas python-dotenv

CMD ["python", "script.py"]