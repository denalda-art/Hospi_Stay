from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
import os
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing, restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"🚨 Model file not found at: {model_path}")

try:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"🚨 Error loading model: {e}")
    model = None

# Define input schema
class InputData(BaseModel):
    age_0_10: float
    department_anesthesia: float
    available_extra_rooms: float

@app.get("/")
def home():
    return {"message": "FastAPI is running. Use /predict to make predictions."}

@app.post("/predict/")
def predict(data: InputData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Check logs.")

    try:
        input_array = np.array([[data.age_0_10, data.department_anesthesia, data.available_extra_rooms]])
        prediction = model.predict(input_array).tolist()
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

