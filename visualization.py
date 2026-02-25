# import folium

# def plot_routes(routes, locations_coords):
#     m = folium.Map(location=[12.97, 77.59], zoom_start=12)  # default coordinates
#     for dest, path in routes.items():
#         coords = [locations_coords[node] for node in path]
#         folium.PolyLine(coords, color='blue', weight=3).add_to(m)
#         folium.Marker(coords[-1], popup=f"{dest}").add_to(m)
#     return m


#2 3
import folium

def plot_routes(routes, locations_coords):
    # Center map at average coordinates
    latitudes = [coord[0] for coord in locations_coords.values()]
    longitudes = [coord[1] for coord in locations_coords.values()]
    map_center = [sum(latitudes)/len(latitudes), sum(longitudes)/len(longitudes)]
    
    m = folium.Map(location=map_center, zoom_start=12)
    
    for dest, path in routes.items():
        coords = [locations_coords[node] for node in path]
        folium.PolyLine(coords, color='blue', weight=3).add_to(m)
        folium.Marker(coords[-1], popup=f"{dest}").add_to(m)
    return m
