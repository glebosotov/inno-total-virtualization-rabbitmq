FROM python:3.10
COPY reader.py /app/reader.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "reader.py"]