from geopy.distance import geodesic
from shapely.geometry import Point

def calculate_distance(coord1, coord2):

    return geodesic(coord1, coord2).km

def extract_features(location, pois):

    distances = []
    if 'geometry' not in pois.columns:
        raise ValueError("POIs GeoDataFrame does not contain a 'geometry' column.")
    
    for _, poi in pois.iterrows():
        if isinstance(poi.geometry, Point):  
            poi_location = (poi.geometry.y, poi.geometry.x)  # Extract latitude and longitude
            distance = calculate_distance(location, poi_location)
            distances.append(distance)
    
    return distances
