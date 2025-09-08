# AI Engineer Hackathon Starter Repository
A starter kit repository for the AI Engineer Hackathon. You can use this repository as a template and develop your solution on the provided structure. This `README.md` should be modified with the information specific to your application.

You should focus on the "Setup Instructions" section to guarantee that following the instructions from start to finish will allow the application to properly initialize and be ready for use. (Try cloning the repository a few times and go through everything line by line before submitting the final solution). The final solution should be present in the `main` branch only, as other branches will not be reviewed during evaluation.

We strongly recommend using Docker Compose during the development, and for submitting the solution. If you are also developing a full frontend (e.g., using React), connect both components using Docker Compose.

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
1. Clone the repository and change directory into it. 
2. Run the following:
```
cp .env.example .env
# Add your OpenAI API key to .env
docker-compose up --build 
```
3. Go to http://127.0.0.1:8000/docs to interact with the endpoints.