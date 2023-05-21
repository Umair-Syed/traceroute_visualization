from pyvis import network as net 

def create_graph(locations, filename):
    print("Create graph called")
    G = net.Network(notebook=True)
    city_colors = {}
    for loc in locations:
        city = loc[3] if loc[3] is not None else "City(Private)"
        if city not in city_colors:
            color = '#{:06x}'.format(hash(city) % 0xffffff)
            city_colors[city] = color
    for loc in locations:
        lat = loc[0]
        lon = loc[1]
        ip = loc[2]
        city = loc[3] if loc[3] is not None else "City(Private)"
        state = loc[4]
        country = loc[5]
        G.add_node(city,node_size=5000, title=(state, country), color=city_colors[city])

    for i in range(len(locations) - 1):
        from_city = locations[i][3] if locations[i][3] is not None else "City(Private)"
        to_city = locations[i+1][3] if locations[i+1][3] is not None else "City(Private)"
        G.add_edge(from_city, to_city, arrows={'to': {'enabled': True, 'type': 'arrow', 'scaleFactor': 0.5}})
        
    G.show(filename)

