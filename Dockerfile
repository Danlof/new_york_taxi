FROM python:3.10

RUN pip install pandas

WORKDIR /app

COPY . . 

ENTRYPOINT ["python3" ,"pipeline.py" ]