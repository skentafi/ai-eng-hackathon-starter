from app.schemas import EstimationRequest, EstimationResponse
from app.services.estimator_logic import CostEstimator


class CostService:
    """
    Service class responsible for handling estimation requests and delegating to the core estimator.
    """

    def __init__(self, assumptions_path: str = "assumptions.yaml"):
        self.estimator = CostEstimator(assumptions_path)

    def estimate(self, request: EstimationRequest) -> EstimationResponse:
        """
        Compute a cost estimate from structured input using the CostEstimator.
        """
        try:
            return self.estimator.estimate(request)
        except Exception as e:
            print(f"[CostService] Error during estimation: {e}")
            raise RuntimeError("Failed to compute cost estimate") from e