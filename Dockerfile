FROM python:3.12-slim

WORKDIR /app

COPY . .
#copy to container

RUN pip install --no-cache-dir -r requirements.txt #run pip to install requirements

EXPOSE 5000

CMD ["sh", "-c", "python app.py"]
