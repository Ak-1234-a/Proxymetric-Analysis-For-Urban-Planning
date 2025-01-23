import osmnx as ox

location = "Madurai, Tamil Nadu, India"
graph = ox.graph_from_place(location, network_type='all')
nodes, edges = ox.graph_to_gdfs(graph) #GeoDataFrames
nodes.to_csv("data/osm_nodes.csv", index=False)
edges.to_csv("data/osm_edges.csv", index=False)
