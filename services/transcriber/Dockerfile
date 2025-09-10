FROM python:3.11-slim



WORKDIR /app

COPY services/Transcriber/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/Transcriber .
COPY utils/decoretors /app/classes
COPY utils/elastic /app/classes
COPY utils/mongo /app/classes
COPY utils/kafka /app/classes



CMD ["python" , "main.py"]