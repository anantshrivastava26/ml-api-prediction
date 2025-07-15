
# TOTAL_FLOW Prediction API (Random Forest)

This project is a **Machine Learning API** built using **FastAPI** and deployed using **Docker** on **AWS ECS**. It predicts the `TOTAL_FLOW` in a gas scrubber system based on several real-time parameters.

---

## 🚀 Project Overview

- **Model Used**: Random Forest Regressor
- **Framework**: FastAPI (Python 3.12)
- **Deployment**: Docker container on AWS ECS (Elastic Container Service)
- **API Type**: RESTful JSON-based POST endpoint
- **Use Case**: Predict gas flow in scrubber systems using live sensor data

---

## 📊 Input Features

The model was trained on the following 43 features:

```

\['BFG\_CO', 'BFG\_CO2', 'BFG\_H2', 'BFG\_PR\_DOWNSTREAM\_1',
'BFG\_PR\_DOWNSTREAM\_2', 'BFG\_PR\_DWNSTRM\_CTRL\_VLV\_POSI\_1',
'BFG\_PR\_DWNSTRM\_CTRL\_VLV\_POSI\_2', 'BFG\_PR\_UPSTREAM\_1',
'BFG\_PR\_UPSTRM\_CTRL\_VLV\_POSI\_1', 'BFG\_PR\_UPSTRM\_CTRL\_VLV\_POSI\_2',
'BFG\_PRESS\_DWNSTRM\_PCV\_8104', 'CLEAN\_GAS\_PR\_AFTER\_DEMESTER',
'CLEAN\_GAS\_TEMP\_AFTER\_DEMISTER', 'AG\_ELEMENT\_1\_POSITION',
'AG\_ELEMENT\_2\_POSITION', 'AG\_ELEMENT\_3\_POSITION',
'BFG\_HP\_NETWORK\_FLOWRATE', 'COLD\_WATER\_SUPPLY\_PR',
'COLD\_WATER\_SUPPLY\_TEMP', 'HYDRAULIC\_OIL\_TEMP',
'PR\_BF\_GAS\_SCRUBBER\_HEAD', 'PRE\_SCRUBBER\_LT\_1', 'PRE\_SCRUBBER\_LT\_2',
'PRE\_SCRUBBER\_LT\_3', 'PRESCRUBBER\_WTR\_CTRL\_VLV\_POSI',
'PRESSURE\_PUMP\_OUTLET\_PR', 'RECIR\_WTR\_CTRL\_VLV\_POSI',
'RECIR\_WATER\_FLOW', 'RECIR\_WATER\_PRESS', 'SCRUBBER\_AG\_LT\_1',
'SCRUBBER\_AG\_LT\_2', 'SCRUBBER\_AG\_LT\_3', 'TEMP\_BF\_GAS\_SCRUBBER\_HEAD',
'Launder\_pH', 'Launder\_Total\_Hardness\_ppm', 'Launder\_Chloride\_ppm',
'Launder\_TSS\_ppm', 'Overflow\_pH', 'Overflow\_Total\_Hardness\_ppm',
'Overflow\_chloride\_ppm', 'Overflow\_TSS\_ppm', 'GCP\_pH',
'GCP\_Total\_Hardness\_ppm', 'GCP\_Chloride\_ppm']

```

---

## 🛠 Project Structure

```

.
├── app.py                  # FastAPI app with prediction logic
├── rf\_model.pkl            # Trained Random Forest model
├── rf\_features.pkl         # List of expected features used during training
├── Dockerfile              # Docker instructions
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

```

---

## 📦 API Usage

### 🟢 Endpoint
```

POST /predict

````

### 📥 Request Body (JSON)

```json
{
  "BFG_CO": 25.698,
  "BFG_CO2": 25.309,
  ...{sample data provided in repo}
  "GCP_Chloride_ppm": 1622.0
}
````

You must include all 43 features (see above) in the request.

### 📤 Response Body (JSON)

```json
{
  "model_used": "random_forest",
  "predicted_TOTAL_FLOW": 2895.31
}
```

---

## 🐳 Docker Instructions

### 1. Build the Docker Image

```bash
docker build -t totalflow-api .
```

### 2. Run the Docker Container

```bash
docker run -p 8000:8000 totalflow-api
```

API will be accessible at:

```
http://localhost:8000/predict
```

---

## ☁️ Deployment on AWS ECS

* Image built and pushed to Amazon ECR
* ECS Task Definition created using the image
* Load Balancer / Security Group configured to allow port `8000`
* FastAPI runs via Uvicorn and listens on `0.0.0.0:8000`

---

## 🧪 Testing (Python)

```python
import requests

url = "http://<your-ecs-ip>:8000/predict"
sample = { "BFG_CO": 25.6, "BFG_CO2": 25.3, ... }  # Complete the 43 features
response = requests.post(url, json=sample)
print(response.json())
```

---

## 📜 License

This project is for educational and internal deployment purposes.

---

## 👨‍💻 Author

**Anant Shrivastava**
🔗 [LinkedIn](https://https://www.linkedin.com/in/anant-shrivastava-b02795251/)

---

```
