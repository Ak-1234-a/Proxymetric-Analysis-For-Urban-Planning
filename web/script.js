let map;
let currentMarker;
let rangeCircle;
let currentLocation = { lat: 51.505, lon: -0.09 }; // Default location

// Set the default range to 1.5 km
const defaultRange = 1.5; // in km

// Initialize the map
function initMap() {
    map = L.map('map').setView([51.505, -0.09], 13); // Default center is set to London

    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Add a default marker to the map
    currentMarker = L.marker([51.505, -0.09]).addTo(map)
        .bindPopup("You are here!")
        .openPopup();

    // Initialize range circle with the default 1.5 km radius
    rangeCircle = L.circle([51.505, -0.09], { radius: defaultRange * 1000 }).addTo(map);

    // Map click listener
    map.on('click', function(e) {
        const lat = e.latlng.lat;
        const lon = e.latlng.lng;
        currentLocation = { lat, lon };
        updateLocationInfo(lat, lon);
        updateMarker(lat, lon);
        updateRange(); // Update range circle to the default value
    });
}

// Get current location of the user
function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;

            currentLocation = { lat, lon };

            // Update map view
            map.setView([lat, lon], 14);

            // Remove any existing marker and add new one
            if (currentMarker) {
                currentMarker.remove();
            }
            currentMarker = L.marker([lat, lon]).addTo(map)
                .bindPopup("You are here!")
                .openPopup();

            // Update location info
            updateLocationInfo(lat, lon);

            // Update range circle with the default 1.5 km radius
            updateRange();
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

// Update location information (latitude, longitude, and address)
function updateLocationInfo(lat, lon) {
    // Display latitude and longitude
    document.getElementById("latitude").innerText = lat;
    document.getElementById("longitude").innerText = lon;

    // Use reverse geocoding to get address from latitude and longitude
    const geocodingUrl = `https://nominatim.openstreetmap.org/reverse?lat=${lat}&lon=${lon}&format=json`;

    fetch(geocodingUrl)
        .then(response => response.json())
        .then(data => {
            const address = data.display_name || "Address not available";
            document.getElementById("address").innerText = address;
        })
        .catch(error => {
            console.error('Error fetching address:', error);
            document.getElementById("address").innerText = "Address not found.";
        });
}

// Update the range circle radius based on the default 1.5 km range
function updateRange() {
    // Update the circle's radius to the default range (1.5 km)
    if (rangeCircle) {
        rangeCircle.setRadius(defaultRange * 1000); // Convert km to meters
    }

    // Center the circle at the current marker location
    rangeCircle.setLatLng([currentLocation.lat, currentLocation.lon]);

    // Optionally call your backend with the static range and location to show proximity prediction
    checkProximity();
}

// Update the marker on the map when user clicks
function updateMarker(lat, lon) {
    if (currentMarker) {
        currentMarker.remove();
    }
    currentMarker = L.marker([lat, lon]).addTo(map)
        .bindPopup("Selected Location")
        .openPopup();
}

// Proximity check function (for backend interaction)
function checkProximity() {
    const lat = currentLocation.lat;
    const lon = currentLocation.lon;

    // Use the default range (1.5 km) here
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "location": [lat, lon],
            "range": defaultRange
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.prediction;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("result").innerText = "An error occurred while checking proximity.";
    });
}

// Initialize the map when the page loads
window.onload = initMap;
