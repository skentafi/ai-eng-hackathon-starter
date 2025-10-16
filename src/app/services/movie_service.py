from app.schemas import CostAssumption, CostEstimate, EstimationResponse
from typing import List, Dict

class CostService:
    # Service class responsible for computing cost estimates from input assumptions

    def __init__(self):
        # No external dependencies needed for initialization
        pass

    def compute_cost(self, assumptions: List[CostAssumption]) -> EstimationResponse:
        """
        Compute total cost and breakdown from a list of cost assumptions.
        Returns a structured EstimationResponse.
        """

        breakdown: Dict[str, float] = {}  # Dictionary to hold per-item costs
        total_cost = 0.0                  # Accumulator for total cost

        try:
            for item in assumptions:
                # Validate assumption fields (optional, since Pydantic already enforces types)
                if item.value < 0:
                    raise ValueError(f"Negative cost value for item: {item.name}")

                # Compute cost per item
                breakdown[item.name] = item.value
                total_cost += item.value

            # Wrap the result in a CostEstimate model
            estimate = CostEstimate(
                total_cost=total_cost,
                breakdown=breakdown
            )

            # Return full response including inputs and computed result
            return EstimationResponse(
                assumptions=assumptions,
                estimate=estimate
            )

        except Exception as e:
            # Graceful fallback in case of unexpected errors
            print(f"[CostService] Error during cost computation: {e}")
            raise RuntimeError("Failed to compute cost estimate") from e
