FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app2.py .
EXPOSE 8000
CMD ["python", "app2.py"]