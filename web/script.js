function predictProximity() {
    var location = document.getElementById("location").value;
    var [lat, lon] = location.split(',');

    // Send location to the backend for prediction
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "location": [parseFloat(lat), parseFloat(lon)]
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.prediction;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
