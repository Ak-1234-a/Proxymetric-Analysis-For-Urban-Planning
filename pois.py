import osmnx as ox

location = "Madurai, Tamil Nadu, India"
tags = {'amenity': ['restaurant', 'school', 'place_of_worship', 'hospital']}
pois = ox.features_from_place(location, tags=tags)
pois.to_file("data/pois.geojson", driver="GeoJSON")
