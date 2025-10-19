# AI Engineer Hackathon Starter Repository

## Application Overview

This repository contains our submission for the AI Engineer Hackathon: a FastAPI-based AI Cost Estimator that predicts project costs based on structured input. The application is containerized with Docker Compose and includes a smoke-tested /estimate endpoint.

The estimator provides a transparent, rule-based cost breakdown for AI system components based on user-defined inputs. It does not rely on any machine learning model or vector database — all logic is defined in code, ensuring full transparency and reproducibility.

## Setup instructions
### Prerequisites

Before running this project, make sure you have the following installed:

- **Docker Engine** - [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose** - [Installation Guide](https://docs.docker.com/compose/install/)

> **Note**: If you're using Docker Desktop, Docker Compose is included automatically.

### Verify Installation
```bash
docker --version
docker compose version 
``` 
### Setup steps   
1. Clone the repository:    
```bash
git clone https://github.com/skentafi/ai-eng-hackathon-starter
```
2. Navigate to the project directory:
```bash
cd ai-eng-hackathon-starter
```
3. Copy the sample `.env` file and fill it with the required credentials:
```bash
cp .env.example .env
# You may override logic variant, currency, or S3 bucket settings here

```
4. Build the Docker images and start all services (first time build):
```bash
docker compose up --build
```   
or 
```bash
docker compose up
```
to start the existing pre-built containers.     
5. Go to http://127.0.0.1:8000/docs to interact with the endpoints.

## Smoke Test Instructions (FastAPI Service)
To verify the containerized service is running and responsive:
1. Run `docker ps` and confirm container is `Up`
2. Open [http://localhost:8000/docs](http://localhost:8000/docs)
3. Send a sample payload to `/estimate` via Swagger or curl
4. Confirm 200 OK and valid response
5. Send `{}` to test error handling — expect 422 Unprocessable Entity

See `docs/smoke-test.md` for full checklist and sample responses.

## To stop the services, run  
```bash
docker compose down
```

## Application description and architecture
For a full breakdown of features, logic flow, and design decisions, see [ARCHITECTURE.md](docs/ARCHITECTURE.md) file. 
