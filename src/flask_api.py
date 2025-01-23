from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to allow cross-origin requests
import pandas as pd
import geopandas as gpd
from model import predict, train_model
from feature_extraction import extract_features

app = Flask(__name__)
CORS(app)  

nodes_path = "./data/osm_nodes.csv"
edges_path = "./data/osm_edges.csv"
pois_path = "./data/pois.geojson"

def load_osm_data_from_files(nodes_file, edges_file):

    nodes = pd.read_csv(nodes_file)
    edges = pd.read_csv(edges_file)
    return nodes, edges

def load_pois_from_file(pois_file):

    pois = gpd.read_file(pois_file)
    return pois

nodes, edges = load_osm_data_from_files(nodes_path, edges_path)
pois = load_pois_from_file(pois_path)

locations = [
    (9.925, 78.119),  # Madurai center
    (9.938, 78.130),  # Another point
    (9.950, 78.100),  # Another location
]
features = [extract_features(loc, pois) for loc in locations]
labels = [1, 0, 1]  


if len(features) > 1:
    model = train_model(features, labels)
else:
    raise ValueError("Not enough samples to train the model. Please add more data.")

@app.route('/predict', methods=['POST'])
def predict_proximity():
    data = request.get_json()
    
    if 'location' not in data:
        return jsonify({'error': 'Location data is missing'}), 400
    
    input_location = tuple(data['location']) 
    
    input_features = extract_features(input_location, pois)
    prediction = predict(model, input_features)
    
    return jsonify({'prediction': "This location is ideal with all essential facilities nearby." if prediction[0] == 1 else "This location lacks sufficient nearby services."})

if __name__ == '__main__':
    app.run(debug=True)
