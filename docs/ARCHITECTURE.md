# 🏗️ Architecture Overview: AI Cost Estimator

This document outlines the architectural decisions, configuration strategy, and estimation logic behind the AI Cost Estimator. The design prioritizes clarity, reproducibility, and ease of deployment — especially in hackathon contexts where reliability and interpretability matter most.

---

## 📦 Repository Structure

```
ai-eng-hackathon-starter/
├── requirements.txt        # Python dependencies  
├── README.md               # Main documentation  
├── .gitignore              # Python + IDE + OS ignores  
├── config.toml             # Project config and default assumptions  
├── docker-compose.yml      # Multi-service setup  
├── Dockerfile              # App container  
├── .env.example            # Environment variables template  
├── docs/  
│   ├── ARCHITECTURE.md     # Architecture notes and rationale  
│   └── smoke-test.md       # Manual smoke test checklist  
├── src/  
│   └── app/  
│       ├── __init__.py         # App module init  
│       ├── config.py           # App settings loader  
│       ├── main.py             # FastAPI entry point  
│       ├── schemas/  
│       │   └── estimator_model.py   # Pydantic request/response models  
│       ├── services/  
│       │   ├── estimator_logic.py   # Core cost estimation logic  
│       │   └── services.py          # Request orchestration and estimation service layer  
│       └── assumptions.yaml    # Cost assumptions (YAML)  
└── data/                       # (Empty) Reserved for sample payloads or test inputs
```
 
---

## 🧩 Module Overview

This section summarizes the core logic modules and their responsibilities:

- `schemas/estimator_model.py`
  Defines the core data models used for request validation and response formatting. See Estimation Schema Overview for field-level details.

- `services/estimator_logic.py`  
  Contains the `CostEstimator` class, which applies rule-based logic to compute total cost and assumptions.

- `services/services.py`  
  Contains the `CostService` class, which orchestrates request handling and delegates computation to `CostEstimator`.

These modules form the backbone of the estimation pipeline and are fully deterministic, ensuring reproducibility and clarity.

---

## 📦 Estimation Schema Overview

The system uses structured Pydantic models to validate inputs and format outputs. These models ensure reproducibility, clarity, and Swagger-based documentation.

### Input Model: EstimationRequest
- `features`: List of capabilities (e.g., inference, retrieval, fine_tuning)
- `usage_scale`: Expected volume (e.g., 1k, 10k, 100k requests)
- `interface`: Access method (e.g., api_endpoint, self_hosted) — affects infrastructure cost logic
- `requirements`: Optional compliance/monitoring flags
- `data_storage`: Storage type (e.g., vector_db, object_storage)

### Output Models
- `CostAssumption`: Each applied cost assumption with name, value, unit, and description
- `CostEstimate`: Final cost breakdown with total and per-category values
- `EstimationResponse`: Combines assumptions and estimate into a structured response

All schemas are defined in `schemas/estimator_model.py` and exposed via Swagger UI at `/docs`.

For full scenario definitions and challenge framing, see the [AI Cost Estimator PRD (Notion)](https://www.notion.so/PRD-team-two-28dbeb2b4c9f80ea9584f2db86e7fbca).

---

## ⚙️ Configuration Strategy

The application uses a layered configuration strategy to balance flexibility with reproducibility:

- **Environment variables** (via `.env`) override runtime behavior
- If `.env` is absent, values are loaded from `config.toml`
- If missing in both, **hardcoded defaults** ensure safe fallback

The `config.toml` file includes:

- Default paths (e.g., to `assumptions.yaml`)
- Service-level toggles (e.g., debug mode)
- Optional overrides for deployment environments

This approach allows seamless deployment while preserving clarity and traceability for reviewers.

---

## 🧠 Estimation Logic

The estimator does **not** rely on any machine learning model or vector database. Instead, all cost calculations are performed using a **transparent, rule-based logic layer** defined in `src/app/services/estimator_logic.py`.

This design ensures:

- ✅ **Reproducibility** — logic is deterministic and inspectable
- ✅ **Interpretability** — reviewers can trace every cost component
- ✅ **Hackathon-readiness** — no external dependencies or model weights required

Cost assumptions are defined in `src/app/assumptions.yaml`, which maps features, usage scales, interfaces, and storage types to cost values. These are loaded at runtime and applied via the `CostEstimator` class.

---

## 🔌 API Wiring

The FastAPI service exposes a single endpoint:

- `POST /estimate` — accepts a structured payload and returns a cost breakdown

The orchestration is handled by `CostService`, which delegates computation to `CostEstimator`. Swagger UI is available at `/docs` for manual testing.

---

## 🧪 Testing Strategy

Manual smoke testing is documented in [`docs/smoke-test.md`](./smoke-test.md). It verifies:

- Container health and logs
- API reachability via Swagger UI
- Minimal payload behavior
- Validation of all three PRD scenarios
- Correct cost breakdown and assumption mapping

---
