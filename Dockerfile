FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only what’s needed
COPY src/ ./src/
COPY data/ ./data/

# Expose FastAPI port
EXPOSE 8000

# Run Uvicorn server (stable, no reload)
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
