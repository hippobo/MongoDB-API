# Using official ubuntu image as a parent image
FROM python:3.9 

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY database.py /code/database.py 

COPY db_requests.py /code/db_requests.py 

COPY main.py /code/main.py 


CMD ["python3", "main.py"]