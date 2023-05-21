import folium
from folium.utilities import validate_location

def plot(locations):
    print("Plot called")
    """Plots locations on a map with different colors based on the city name."""
    # Initialize the map
    m = folium.Map(location=[0, 0], zoom_start=2)
    
    for coord in locations:
        lat, lon, ip, city, state, country = coord
        popup_text = f"{city}, {state}, {country}"
        folium.Marker(location=validate_location((lat, lon)), popup=popup_text).add_to(m)

    # Create a color map based on the city name
    city_colors = {}
    for loc in locations:
        city = loc[3]
        if city not in city_colors:
            color = '#{:06x}'.format(hash(city) % 0xffffff) 
            city_colors[city] = color

    # Assign a color to each marker based on its city name
    for coord in locations:
        city = coord[3]
        color = city_colors[city]
        folium.CircleMarker(location=validate_location(coord[:2]), radius=8, color=color, fill_color=color).add_to(m)
    for i in range(len(locations)-1):
        start = validate_location(locations[i][:2])
        end = validate_location(locations[i+1][:2])
        city = locations[i][3]
        color = city_colors[city]
        folium.PolyLine([start, end], color=color).add_to(m)
    # Create a legend based on the city colors
    legend_html = '<div style="position: fixed; bottom: 50px; left: 50px; z-index:9999; font-size:14px;">'
    for city, color in city_colors.items():
        legend_html += f'<p><span style="background-color:{color};padding:5px;border-radius:50%;">&nbsp;&nbsp;&nbsp;&nbsp;</span> {city}</p>'
    legend_html += '</div>'
    m.get_root().html.add_child(folium.Element(legend_html))
    m.save('mainapp/templates/map.html')
