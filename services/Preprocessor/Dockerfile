FROM python:3.11-slim


WORKDIR /app

RUN mkdir /podcasts

WORKDIR /app
              
COPY services/Preprocessor/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/Preprocessor .
COPY utils/decoretors /app/classes

COPY utils/kafka /app/classes


CMD ["python" , "main.py"]