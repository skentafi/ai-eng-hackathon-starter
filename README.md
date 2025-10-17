# AI Engineer Hackathon Starter Repository
A starter kit repository for the AI Engineer Hackathon. You can use this repository as a template and develop your solution on the provided structure. This `README.md` should be modified with the information specific to your application.

You should focus on the "Setup Instructions" section to guarantee that following the instructions from start to finish will allow the application to properly initialize and be ready for use. (Try cloning the repository a few times and go through everything line by line before submitting the final solution). The final solution should be present in the `main` branch only, as other branches will not be reviewed during evaluation.

We strongly recommend using Docker Compose during the development (`docker-compose.yml` in this repository is the development version with hot reload for the FastAPI server), and for submitting the solution. If you are also developing a full frontend (e.g., using React), connect both components using Docker Compose. 

Initial repository structure:
```
ai-eng-hackathon-starter/
├── README.md                   # Main documentation
├── .gitignore                  # Python + IDE + OS ignores
├── config.toml                 # Project config 
├── docker-compose.yml          # Multi-service setup
├── Dockerfile                  # App container
├── .env.example                # Environment variables template
├── docs/
│   └── ARCHITECTURE.md        # A detailed explanation/ analysis of the app architecture
├── src/
│   └── app/
│       ├── __init__.py
|       ├── config.py         # Managment for the app settings
│       ├── main.py           # FastAPI app entry point
│       ├── schemas/          # Pydantic models
│       └── utils/            
└── data/                     # Sample data
```

The application is a simple semantic search engine for movies. It can add movies into the collection and perform semantic search through the existing database. 

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
git clone https://github.com/hyperskill-content/ai-eng-hackathon-starter
```
2. Navigate to the project directory:
```bash
cd ai-eng-hackathon-starter
```
3. Copy the sample `.env` file and fill it with the required credentials:
```bash
cp .env.example .env
# Add your OpenAI API key to .env
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

To stop the services and remove volumes (if needed), run  
```bash
docker compose down
# or docker compose down -v to remove the created volumes
```

## Application description and architecture 
Explanations of features, detected areas for improvement, product development plan, and system design of the app should be described in [ARCHITECTURE.md](docs/ARCHITECTURE.md) file. 

## Smoke Test Instructions (FastAPI Service)
To verify the containerized service is running and responsive:
1. Run `docker ps` and confirm container is `Up`
2. Open [http://localhost:8000/docs](http://localhost:8000/docs)
3. Send a sample payload to `/estimate` via Swagger or curl
4. Confirm 200 OK and valid response
5. Send `{}` to test error handling — expect 422 Unprocessable Entity

See `docs/smoke-test.md` for full checklist and sample responses.
