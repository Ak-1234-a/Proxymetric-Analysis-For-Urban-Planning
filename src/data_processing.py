import pandas as pd
import geopandas as gpd

def load_osm_data_from_files(nodes_path, edges_path):
    """
    Loads OSM node and edge data from CSV files.
    
    Args:
        nodes_path (str): Path to the OSM nodes CSV file.
        edges_path (str): Path to the OSM edges CSV file.
        
    Returns:
        nodes (GeoDataFrame): GeoDataFrame of OSM nodes.
        edges (GeoDataFrame): GeoDataFrame of OSM edges.
    """
    nodes = pd.read_csv(nodes_path)
    edges = pd.read_csv(edges_path)
    
    # Convert the nodes DataFrame to a GeoDataFrame using geometry column
    nodes = gpd.GeoDataFrame(nodes, geometry=gpd.points_from_xy(nodes['longitude'], nodes['latitude']))
    
    # Convert the edges DataFrame to a GeoDataFrame
    edges = gpd.GeoDataFrame(edges, geometry=gpd.GeoSeries.from_wkt(edges['geometry']))
    
    return nodes, edges

def load_pois_from_file(pois_path):
    """
    Loads Points of Interest (POIs) from a GeoJSON file.
    
    Args:
        pois_path (str): Path to the POIs GeoJSON file.
        
    Returns:
        pois (GeoDataFrame): GeoDataFrame of POIs.
    """
    pois = gpd.read_file(pois_path)
    return pois
