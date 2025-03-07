window.onload = function () {
    let form = document.getElementById("predictForm");
    if (!form) {
        console.error("❌ Error: predictForm not found. Make sure the form ID is correct.");
        return;
    }

    document.getElementById("predict-btn").addEventListener("click", async function () {
        let age_0_10 = document.getElementById("age_0_10").value;
        let department_anesthesia = document.getElementById("department_anesthesia").value;
        let available_extra_rooms = document.getElementById("available_extra_rooms").value;

        let payload = {
            age_0_10: Number(age_0_10),
            department_anesthesia: Number(department_anesthesia),
            available_extra_rooms: Number(available_extra_rooms)
        };

        console.log("📤 Sending to API:", payload);

        try {
            let response = await fetch("https://hospistay-production.up.railway.app/predict/", { 
                method: "POST",
                headers: { "Content-Type": "application/json" },
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

