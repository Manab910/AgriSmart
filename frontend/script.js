const predictBtn = document.getElementById("predictBtn");
const loader = document.getElementById("loader");
const icons = {
    rice: "🌾",
    wheat: "🌾",
    maize: "🌽",
    corn: "🌽",
    cotton: "☁️",
    coconut: "🥥",
    banana: "🍌",
    mango: "🥭",
    grapes: "🍇",
    apple: "🍎",
    orange: "🍊",
    papaya: "🍈",
    pomegranate: "🍎",
    coffee: "☕",
    jute: "🌿"
};
predictBtn.addEventListener("click", async () => {

    // Get input values
    const N = document.getElementById("nitrogen").value;
    const P = document.getElementById("phosphorus").value;
    const K = document.getElementById("potassium").value;
    const temperature = document.getElementById("temperature").value;
    const humidity = document.getElementById("humidity").value;
    const ph = document.getElementById("ph").value;
    const rainfall = document.getElementById("rainfall").value;

    // Validation
    if (
        N === "" ||
        P === "" ||
        K === "" ||
        temperature === "" ||
        humidity === "" ||
        ph === "" ||
        rainfall === ""
    ) {
        alert("Please fill in all the fields.");
        return;
    }

    // Show loading state
    predictBtn.disabled = true;
    predictBtn.innerHTML = "Predicting...";

    loader.classList.remove("hidden");

    document.getElementById("cropName").innerHTML = "Analyzing...";
    document.getElementById("predictionMessage").innerHTML =
        "Our AI model is analyzing your soil and weather data...";

    document.getElementById("confidence").innerHTML = "--";
    document.getElementById("displayTemp").innerHTML = "--";
    document.getElementById("displayHumidity").innerHTML = "--";
    document.getElementById("displayRainfall").innerHTML = "--";
try {

    const data = {
        N: Number(N),
        P: Number(P),
        K: Number(K),
        temperature: Number(temperature),
        humidity: Number(humidity),
        ph: Number(ph),
        rainfall: Number(rainfall)
    };

    const response = await fetch(
        "https://agri-smart-gamma.vercel.app/predict-crop",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status}`);
    }

    const result = await response.json();

    const crop = document.getElementById("cropName");
    const cropIcon = document.getElementById("cropIcon");

    cropIcon.innerHTML =
        icons[result.recommended_crop.toLowerCase()] || "🌱";

    crop.innerHTML = result.recommended_crop;

    crop.classList.add("success");

    setTimeout(() => {
        crop.classList.remove("success");
    }, 400);

    document.getElementById("predictionMessage").innerHTML =
        result.message ||
        "The AI model recommends this crop based on your soil and environmental conditions.";

    document.getElementById("confidence").innerHTML =
        result.confidence !== undefined
            ? result.confidence + "%"
            : "Available Soon";

    document.getElementById("displayTemp").innerHTML =
        (result.temperature ?? temperature) + " °C";

    document.getElementById("displayHumidity").innerHTML =
        (result.humidity ?? humidity) + " %";

    document.getElementById("displayRainfall").innerHTML =
        (result.rainfall ?? rainfall) + " mm";

} catch (error) {

    console.error(error);

    document.getElementById("cropName").innerHTML = "Prediction Failed";

    document.getElementById("predictionMessage").innerHTML =
        error.message;

    document.getElementById("confidence").innerHTML = "--";
    document.getElementById("displayTemp").innerHTML = "--";
    document.getElementById("displayHumidity").innerHTML = "--";
    document.getElementById("displayRainfall").innerHTML = "--";

} finally {

        loader.classList.add("hidden");

        predictBtn.disabled = false;

        predictBtn.innerHTML =
            'Predict Optimal Crop <i class="fa-solid fa-arrow-right"></i>';

    }

});
