from pydantic import BaseModel
from typing import List, Dict
from enum import Enum

# === ENUMS FOR INPUT SCHEMA ===

class Feature(str, Enum):
    inference = "inference"
    retrieval = "retrieval"
    fine_tuning = "fine_tuning"

class Requirement(str, Enum):
    monitoring = "monitoring"
    compliance = "compliance"

class UsageScale(str, Enum):
    one_k = "1k_requests"
    ten_k = "10k_requests"
    hundred_k = "100k_requests"

class DataStorage(str, Enum):
    vector_db = "vector_db"
    object_storage = "object_storage"

class Interface(str, Enum):
    api_endpoint = "api_endpoint"
    self_hosted = "self_hosted"


# === INPUT MODEL ===

class EstimationRequest(BaseModel):
    features: List[Feature]
    usage_scale: UsageScale
    interface: Interface
    requirements: List[Requirement]
    data_storage: DataStorage


# === OUTPUT MODELS ===

class CostAssumption(BaseModel):
    name: str
    value: float
    unit: str
    description: str

class CostEstimate(BaseModel):
    total_cost: float
    breakdown: Dict[str, float]

class EstimationResponse(BaseModel):
    assumptions: List[CostAssumption]
    estimate: CostEstimate
