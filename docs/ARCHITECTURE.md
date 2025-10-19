# 🏗️ Architecture Overview: AI Cost Estimator

This document outlines the architectural decisions, configuration strategy, and estimation logic behind the AI Cost Estimator. The design prioritizes clarity, reproducibility, and ease of deployment — especially in hackathon contexts where reliability and interpretability matter most.

---

## 📦 Repository Structure

<pre>
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
</pre>
 
---

## 🧩 Module Overview

This section summarizes the core logic modules and their responsibilities:

- `schemas/estimator_model.py`  
  Defines the Pydantic models for request validation and response formatting.

- `services/estimator_logic.py`  
  Contains the `CostEstimator` class, which applies rule-based logic to compute total cost and assumptions.

- `services/services.py`  
  Contains the `CostService` class, which orchestrates request handling and delegates computation to `CostEstimator`.

These modules form the backbone of the estimation pipeline and are fully deterministic, ensuring reproducibility and clarity.

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
- Minimal valid payload behavior
- Correct cost breakdown and assumption mapping

This ensures the service is demo-ready and behaves predictably under expected inputs.

---
