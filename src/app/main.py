from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from app.schemas import EstimationRequest, EstimationResponse
from app.services import CostService

cost_service = CostService()

@asynccontextmanager
async def lifespan(_app: FastAPI):
    print("Cost Estimator service initialized")
    yield
    print("Cost Estimator service shutting down")

app = FastAPI(title="AI Cost Estimator", version="1.0.0", lifespan=lifespan)

@app.post("/estimate", response_model=EstimationResponse)
async def estimate_cost(request: EstimationRequest):
    try:
        return cost_service.estimate(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
