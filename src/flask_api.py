from flask import Flask, request, jsonify
from model import predict, train_model
from feature_extraction import extract_features
from data_processing import get_pois, download_osm_data

app = Flask(__name__)

# Load data and train model on startup (simplified for this example)
location = "Madurai, Tamil Nadu, India"  # Example location to fetch initial POIs
nodes, edges = download_osm_data(location)
pois = get_pois(location)

# Extract features from POIs (simplified)
# Use actual latitude and longitude values for the initial training
features = [extract_features((9.925, 78.119), pois)]  # Example: feature extraction for Madurai
labels = [1]  # Dummy labels for simplicity (1 = well-connected)

# Train the model
model = train_model(features, labels)

@app.route('/predict', methods=['POST'])
def predict_proximity():
    # Get data from the user
    data = request.get_json()
    location = data['location']  # Example: {"location": [9.925, 78.119]}

    # Extract latitude and longitude from the input location
    lat, lon = location

    # Download POIs and extract features for the input location
    pois = get_pois(f"{lat},{lon}")
    input_features = extract_features((lat, lon), pois)
    
    # Predict the connectivity status
    prediction = predict(model, input_features)
    
    # Return result as JSON response
    return jsonify({'prediction': "Well-connected" if prediction[0] == 1 else "Poorly connected"})

if __name__ == '__main__':
    app.run(debug=True)
