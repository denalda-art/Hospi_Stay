window.onload = function () {
    let form = document.getElementById("predictForm");
    if (!form) {
        console.error("❌ Error: predictForm not found. Make sure the form ID is correct.");
        return;
    }

    document.getElementById("predict-btn").addEventListener("click", async function (event) {
        event.preventDefault();

        let age = document.getElementById("age").value;
        let department = document.getElementById("department").value;
        let rooms = document.getElementById("rooms").value;

        let payload = {
            age_0_10: Number(age),
            department_anesthesia: Number(department),
            available_extra_rooms: Number(rooms)
        };

        console.log("📤 Sending to FastAPI:", payload);

        try {
            let response = await fetch("http://127.0.0.1:8000/predict/", { // Ensure FastAPI URL
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });

            console.log("📥 Response received:", response);

            if (!response.ok) {
                throw new Error(`Server error: ${response.status} - ${response.statusText}`);
            }

            let jsonResponse = await response.json();
            console.log("✅ JSON Response:", jsonResponse);

            document.getElementById("prediction-result").innerText = "Predicted Value: " + jsonResponse.prediction;
        } catch (error) {
            console.error("❌ Error:", error.message);
            document.getElementById("prediction-result").innerText = "❌ Error: " + error.message;
        }
    });
};

