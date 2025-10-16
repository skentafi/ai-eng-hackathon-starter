from pydantic import BaseModel
from typing import List, Dict

class CostAssumption(BaseModel):
    """
    Represents a single cost input used in the estimation.
    """
    name: str         # Identifier for the cost item (e.g., "compute", "storage")
    value: float      # Numeric cost value (e.g., 12.5)
    unit: str         # Unit of measurement (e.g., "USD/hr", "USD/GB")
    description: str  # Human-readable explanation of the cost item

class CostEstimate(BaseModel):
    """
    Represents the computed result of the cost estimation.
    """
    total_cost: float           # Sum of all cost values
    breakdown: Dict[str, float] # Per-item cost breakdown (e.g., {"compute": 12.5})

class EstimationResponse(BaseModel):
    """
    Wraps the full response to a cost estimation request.
    """
    assumptions: List[CostAssumption]  # List of input assumptions used for estimation
    estimate: CostEstimate             # Final computed cost result
