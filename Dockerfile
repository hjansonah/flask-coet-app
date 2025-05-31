# → Dockerfile (C:\Users\user\Documents\Coets-flask-backend\Dockerfile)

# 1) Use a lightweight Python 3.11 image
FROM python:3.11-slim

# 2) Prevent Python from writing *.pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3) Set working directory
WORKDIR /app

# 4) Copy requirements and install them
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 5) Copy the rest of the app’s source code
COPY . /app/

# 6) Expose port 8080 (must match PORT in fly.toml/env)
EXPOSE 8080

# 7) Use Gunicorn to serve the app
#    - bind to 0.0.0.0:$PORT
#    - use 2 worker processes (adjust as needed)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
