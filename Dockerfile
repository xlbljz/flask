FROM python:3.11.0
WORKDIR /app
COPY . .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
EXPOSE 80