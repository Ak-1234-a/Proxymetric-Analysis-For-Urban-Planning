import pandas as pd
import geopandas as gpd

def load_osm_data_from_files(nodes_path, edges_path):

    nodes = pd.read_csv(nodes_path)
    edges = pd.read_csv(edges_path)
    
    nodes = gpd.GeoDataFrame(nodes, geometry=gpd.points_from_xy(nodes['longitude'], nodes['latitude']))
    
    edges = gpd.GeoDataFrame(edges, geometry=gpd.GeoSeries.from_wkt(edges['geometry']))
    
    return nodes, edges

def load_pois_from_file(pois_path):

    pois = gpd.read_file(pois_path)
    return pois
