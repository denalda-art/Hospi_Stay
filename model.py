import pandas as pd
import joblib

# Load the trained model
model = joblib.load("/Users/denaldakuzumi/RapidMinerScripts/model.pkl")

def rm_main(data):
    print("✅ Received data from RapidMiner:")
    print(data.head())
    print("✅ Columns in received data:", list(data.columns))

    # Mapping detailed feature names to generic ones used during training
    rename_map = {
        "Age = 0-10": "feature1",
        "Department = anesthesia": "feature2",
        "Available Extra Rooms in Hospital": "feature3"
    }

    # Rename columns to match the model's training features
    data = data.rename(columns=rename_map)

    # Ensure only the expected model features are present
    expected_features = ["feature1", "feature2", "feature3"]
    missing_cols = [col for col in expected_features if col not in data.columns]
    if missing_cols:
        raise ValueError(f"🚨 Mismatch! Missing columns: {missing_cols}")

    # Make prediction
    predictions = model.predict(data[expected_features])

    # Add predictions
    data["prediction"] = predictions

    print("✅ Predictions generated successfully!")
    return data  # Return DataFrame to RapidMiner

print("✅ Script executed successfully!")
