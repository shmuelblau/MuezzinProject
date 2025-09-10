FROM python:3.11-slim



WORKDIR /app

COPY services/Classifierd/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/Classifierd .
COPY utils/decoretors /app/classes
COPY utils/elastic /app/classes





CMD ["python" , "main.py"]