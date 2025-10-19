# Smoke Test Checklist: FastAPI Cost Estimator (Dockerized)

This checklist verifies that the containerized FastAPI service is running, responsive, and correctly wired to serve `/estimate` with valid assumptions.

---

## 1. Container Health Check

- Run: `docker ps`  
- Confirm container is **Up** and named `ai-cost-estimator`  
- Run: `docker logs ai-cost-estimator`  
- Look for: `Uvicorn running on http://0.0.0.0:8000`

---

## 2. API Reachability

- Open: [http://localhost:8000/docs](http://localhost:8000/docs)  
- Confirm Swagger UI loads  
- Click `/estimate` → Try it out  
- Paste sample payload (see below)  
- Click **Execute**  
- Confirm `200 OK` and valid JSON response  
- Send `{}` to test error handling — expect `422 Unprocessable Entity`

---

## 3. Minimal Payload & PRD Scenario Validation

### Minimal Payload:

Paste this payload into Swagger or curl:
```
json
{
  "features": ["inference"],
  "usage_scale": "1k_requests",
  "interface": "api_endpoint",
  "requirements": ["monitoring"],
  "data_storage": "vector_db"
}
```

Expected total: 810 USD  
Assumptions: inference, vector_db, monitoring

Note: The minimal payload shares structure with Scenario 1 but uses vector_db for lightweight validation. Scenario 1 reflects a realistic PM configuration with object_storage.

### Scenario 1: Product Manager Sanity Check
```
json
{
  "features": ["inference"],
  "usage_scale": "1k_requests",
  "interface": "api_endpoint",
  "requirements": ["monitoring"],
  "data_storage": "object_storage"
}
```

Expected total: 810 USD   
Assumptions: inference, object_storage, monitoring

### Scenario 2: Engineer Planning Infrastructure
```
json
{
  "features": ["fine_tuning"],
  "usage_scale": "10k_requests",
  "interface": "self_hosted",
  "requirements": ["compliance"],
  "data_storage": "object_storage"
}
```

Expected total: 4,100 USD   
Assumptions: fine_tuning, object_storage, compliance

### Scenario 3: Founder Evaluating Feasibility
```
json
{
  "features": ["retrieval"],
  "usage_scale": "1k_requests",
  "interface": "api_endpoint",
  "requirements": ["monitoring"],
  "data_storage": "vector_db"
}
```

Expected total: 600 USD  
Assumptions: retrieval, vector_db, monitoring
