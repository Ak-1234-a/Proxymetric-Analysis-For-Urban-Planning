from geopy.distance import geodesic
from shapely.geometry import Point

def calculate_distance(coord1, coord2):
    """
    Calculates the distance between two geographic coordinates using geodesic.
    """
    return geodesic(coord1, coord2).km

def extract_features(location, pois):
    """
    Extracts features such as distances to nearby amenities (restaurants, schools, temples).
    
    Args:
        location (tuple): A tuple of (latitude, longitude) for the target location.
        pois (GeoDataFrame): A GeoDataFrame containing Points of Interest (POIs) with a geometry column.
    
    Returns:
        list: A list of distances from the location to each POI in kilometers.
    """
    distances = []
    if 'geometry' not in pois.columns:
        raise ValueError("POIs GeoDataFrame does not contain a 'geometry' column.")
    
    for _, poi in pois.iterrows():
        if isinstance(poi.geometry, Point):  # Ensure the geometry is a valid Point
            poi_location = (poi.geometry.y, poi.geometry.x)  # Extract latitude and longitude
            distance = calculate_distance(location, poi_location)
            distances.append(distance)
    
    return distances
