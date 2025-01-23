# Proximity Analysis System For Urban Planning

  This project analyzes the proximity and connectivity of a given location based on nearby amenities and infrastructure. Using OpenStreetMap (OSM) data, it calculates features like distances to Points of Interest (POIs) and predicts if the location is "perfectly connected with amenities" or "poorly connected."


## Features

**OSM Integration:** Extracts nodes, edges, and POIs from OSM for a specified location.

**Feature Extraction:** Calculates distances to amenities like schools, restaurants, and places of worship.

**Machine Learning:** Uses Random Forest Classifier to classify locations as well-connected or poorly connected.

**Flask API:** Provides an endpoint to input a location and get connectivity predictions.


## Folder Structure
```
project/
├── data/
│   ├── osm_nodes.csv       # Nodes data from OSM
│   ├── osm_edges.csv       # Edges data from OSM
│   └── pois.geojson        # Points of Interest data
├── src/
│   ├── flask_api.py        # Flask server code
│   ├── data_processing.py  # Handles OSM data loading and processing
│   ├── feature_extraction.py  # Extracts proximity and amenity-related features
│   ├── model.py            # Trains and predicts using Random Forest Classifier model
│   └── requirements.txt    # Python dependencies
└── README.md               # Project documentation
```

## Requirements
```
Python 3.9+

Flask

scikit-learn

geopandas

osmnx

geopy
```

Install dependencies using:

```pip install -r requirements.txt```

## How It Works

1. **OSM Data:** Downloads nodes, edges, and POIs for the specified location using OSM APIs.


2. **Feature Extraction:** Calculates distances from a given location to nearby amenities.


3. **Model Training:** Trains a Random Forest Classifier model on labeled examples to classify locations.


4. **API Prediction:** Takes a location as input via the Flask API and returns whether it is "perfectly connected with amenities" or not.



## Usage

1. Place the dataset files (`osm_nodes.csv, osm_edges.csv, and pois.geojson`) in the data/ folder.

2. Start the Flask server:

    ```python src/flask_api.py```

3. Use the `/predict` endpoint to get predictions. Example:

```
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"location": [9.925, 78.119]}'
```
4. First choose "**Use My Current Location**" and then choose any area from madurai and explore it.


## Contribution

1. Moulesh G S
2. Janarthanan C
3. Vivek Ram Prakash 
4. Arun Kumar J E
5. Vigneshwarlal 

