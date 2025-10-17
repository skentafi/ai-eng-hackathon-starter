from pydantic import BaseModel
from typing import List, Dict
from enum import Enum
import yaml
from datetime import datetime


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


# === CORE ESTIMATOR LOGIC ===

class CostEstimator:
    def __init__(self, assumptions_path: str = "assumptions.yaml"):
        with open(assumptions_path, "r") as f:
            self.assumptions = yaml.safe_load(f)

    def estimate(self, request: EstimationRequest) -> EstimationResponse:
        model_cost = sum(self.assumptions["model"][feature.value] for feature in request.features)
        data_cost = self.assumptions["data"][request.data_storage.value]
        infra_cost = sum(self.assumptions["infrastructure"][req.value] for req in request.requirements)

        usage_multiplier = {
            UsageScale.one_k: 1,
            UsageScale.ten_k: 10,
            UsageScale.hundred_k: 100
        }[request.usage_scale]

        total_model = model_cost * usage_multiplier
        total_data = data_cost * usage_multiplier
        total_infra = infra_cost

        total = total_model + total_data + total_infra

        breakdown = {
            "model": round(total_model, 2),
            "data": round(total_data, 2),
            "infrastructure": round(total_infra, 2)
        }

        assumptions_list = [
            CostAssumption(
                name=feature.value,
                value=self.assumptions["model"][feature.value],
                unit="USD/request",
                description=f"Model feature: {feature.value}"
            )
            for feature in request.features
        ] + [
            CostAssumption(
                name=request.data_storage.value,
                value=data_cost,
                unit="USD/GB",
                description="Data storage type"
            )
        ] + [
            CostAssumption(
                name=req.value,
                value=self.assumptions["infrastructure"][req.value],
                unit="USD/month",
                description=f"Infrastructure requirement: {req.value}"
            )
            for req in request.requirements
        ]

        return EstimationResponse(
            assumptions=assumptions_list,
            estimate=CostEstimate(
                total_cost=round(total, 2),
                breakdown=breakdown
            )
        )
