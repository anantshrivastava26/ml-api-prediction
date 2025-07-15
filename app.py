from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.responses import JSONResponse
import uvicorn ##ASGI
# Load model and features
model = joblib.load("rf_model.pkl")
expected_features = joblib.load("rf_features.pkl")

# Define Pydantic model with exact features
class FlowInput(BaseModel):
    BFG_CO: float
    BFG_CO2: float
    BFG_H2: float
    BFG_PR_DOWNSTREAM_1: float
    BFG_PR_DOWNSTREAM_2: float
    BFG_PR_DWNSTRM_CTRL_VLV_POSI_1: float
    BFG_PR_DWNSTRM_CTRL_VLV_POSI_2: float
    BFG_PR_UPSTREAM_1: float
    BFG_PR_UPSTRM_CTRL_VLV_POSI_1: float
    BFG_PR_UPSTRM_CTRL_VLV_POSI_2: float
    BFG_PRESS_DWNSTRM_PCV_8104: float
    CLEAN_GAS_PR_AFTER_DEMESTER: float
    CLEAN_GAS_TEMP_AFTER_DEMISTER: float
    AG_ELEMENT_1_POSITION: float
    AG_ELEMENT_2_POSITION: float
    AG_ELEMENT_3_POSITION: float
    BFG_HP_NETWORK_FLOWRATE: float
    COLD_WATER_SUPPLY_PR: float
    COLD_WATER_SUPPLY_TEMP: float
    HYDRAULIC_OIL_TEMP: float
    PR_BF_GAS_SCRUBBER_HEAD: float
    PRE_SCRUBBER_LT_1: float
    PRE_SCRUBBER_LT_2: float
    PRE_SCRUBBER_LT_3: float
    PRESCRUBBER_WTR_CTRL_VLV_POSI: float
    PRESSURE_PUMP_OUTLET_PR: float
    RECIR_WTR_CTRL_VLV_POSI: float
    RECIR_WATER_FLOW: float
    RECIR_WATER_PRESS: float
    SCRUBBER_AG_LT_1: float
    SCRUBBER_AG_LT_2: float
    SCRUBBER_AG_LT_3: float
    TEMP_BF_GAS_SCRUBBER_HEAD: float
    Launder_pH: float
    Launder_Total_Hardness_ppm: float
    Launder_Chloride_ppm: float
    Launder_TSS_ppm: float
    Overflow_pH: float
    Overflow_Total_Hardness_ppm: float
    Overflow_chloride_ppm: float
    Overflow_TSS_ppm: float
    GCP_pH: float
    GCP_Total_Hardness_ppm: float
    GCP_Chloride_ppm: float

# FastAPI app
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to TOTAL_FLOW Prediction API (Random Forest)"}

@app.post("/predict")
def predict(input_data: FlowInput):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data.dict()])
        input_df = input_df.reindex(columns=expected_features)
        prediction = model.predict(input_df)[0]
        prediction = prediction.item()  # ensure native Python float
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

    return JSONResponse(
        content={
            "model_used": "random_forest",
            "predicted_TOTAL_FLOW": prediction
        }
    )
if __name__ == "__app__":
    uvicorn.run(app, host="127.0.0.1:8000", port=8000)
# To run the server, use the command: uvicorn app:app --reload