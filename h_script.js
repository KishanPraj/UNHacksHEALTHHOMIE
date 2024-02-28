async function submitSymptoms() {
    const data = {
        Pregnancies: document.getElementById('Pregnancies').value,
        Glucose: document.getElementById('Glucose').value,
        BloodPressure: document.getElementById('BloodPressure').value,
        Insulin: document.getElementById('Insulin').value,
        BMI: document.getElementById('BMI').value,
        Age: document.getElementById('Age').value,
    };

    try {
        const response = await fetch('http://localhost:5000/predictdiabetes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const responseData = await response.json();
		
	    const jsonData = JSON.parse(JSON.stringify(responseData)); // Parsing the JSON string to an object
	    const prediction = jsonData.prediction; // Extracting the thumbnail URL
	 	document.getElementById('recommendation').innerText = prediction;
 
    } catch (error) {
        console.error('Error:', error);
    }
}

async function submitHeartSymptoms() {
	
	console.log("aaaa");
	
	
    const data = {
        age: document.getElementById('age').value,
        sex: document.getElementById('sex').value,
        chest_pain_type: document.getElementById('chest_pain_type').value,
        resting_bp: document.getElementById('resting_bp').value,
        cholestoral: document.getElementById('cholestoral').value,
        fasting_blood_sugar: document.getElementById('fasting_blood_sugar').value,
        restecg: document.getElementById('restecg').value,
        max_hr: document.getElementById('max_hr').value,
        exang: document.getElementById('exang').value,
        oldpeak: document.getElementById('oldpeak').value,
        slope: document.getElementById('slope').value,
        num_major_vessels: document.getElementById('num_major_vessels').value,
        thal: document.getElementById('thal').value,
    };
	
	console.log("aaaa");

    try {
        const response = await fetch('http://localhost:5000/predictheartdisease', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const responseData = await response.json();
		
	    const jsonData = JSON.parse(JSON.stringify(responseData)); // Parsing the JSON string to an object
	    const prediction = jsonData.prediction; 
	 	document.getElementById('recommendation').innerText = prediction;
 
    } catch (error) {
        console.error('Error:', error);
    }
}
