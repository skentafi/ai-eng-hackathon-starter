FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the app logic and assumptions.yaml
COPY src/app/assumptions.yaml .
COPY src/app/ ./app/

# Expose FastAPI port
EXPOSE 8000

# Run Uvicorn server (stable, no reload)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]