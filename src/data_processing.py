import osmnx as ox
import geopandas as gpd

def download_osm_data(location_name):
    """
    Downloads OSM data for the specified location (e.g., a city).
    """
    print(f"Downloading OSM data for {location_name}...")
    graph = ox.graph_from_place(location_name, network_type='all')
    nodes, edges = ox.graph_to_gdfs(graph)
    return nodes, edges

def get_pois(location_name, tags={'amenity': ['restaurant', 'school', 'place_of_worship']}):
    """
    Downloads Points of Interest (POIs) like restaurants, schools, temples from OSM.
    """
    print(f"Downloading POIs for {location_name}...")
    pois = ox.features_from_place(location_name, tags=tags)
    
    if pois.empty:
        print(f"No POIs found for {location_name}. Try adjusting tags or location.")
    else:
        print(f"Found {len(pois)} POIs.")
    return pois


