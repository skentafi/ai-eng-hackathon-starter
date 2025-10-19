# Smoke Test Checklist: FastAPI Cost Estimator (Dockerized)

This checklist verifies that the containerized FastAPI service is running, responsive, and correctly wired to serve `/estimate` with valid assumptions.

---

## 1. Container Health Check

- Run: `docker ps`
  - Confirm container is `Up` and named `ai-cost-estimator`
- Run: `docker logs ai-cost-estimator`
  - Look for: `Uvicorn running on http://0.0.0.0:8000`

---

## 2. API Reachability

- Open: [http://localhost:8000/docs](http://localhost:8000/docs)
  - Confirm Swagger UI loads
- Click `/estimate` → **Try it out**
  - Paste sample payload (see below)
  - Click **Execute**
  - Confirm 200 OK and valid JSON response

---

## 3. Minimal Valid Payload Test

### Quick Test via Swagger
This test verifies that the /estimate endpoint accepts a minimal valid payload and returns a correct cost breakdown.
1. Run the service: `docker compose up --build`
2. Open: http://localhost:8000/docs
3. Click `/estimate` → **Try it out**
4. Paste this payload:

```json
{
  "features": ["inference"],
  "usage_scale": "1k_requests",
  "interface": "api_endpoint",
  "requirements": ["monitoring"],
  "data_storage": "vector_db"
}

5. Click Execute

6. Confirm the response includes:

"total_cost": 50.1

"assumptions" list with:

"inference"

"vector_db"

"monitoring"