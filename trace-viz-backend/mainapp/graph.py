import mpld3
import os
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# def create_graph(locations, filename):
#     # Initialize a directed graph
#     G = nx.DiGraph()

#     # Add nodes for each city
#     for loc in locations:
#         lat = loc[0]
#         lon = loc[1]
#         ip = loc[2]
#         city = loc[3]
#         state = loc[4]
#         country = loc[5]
#         G.add_node(city, lat=lat, lon=lon, ip=ip, state=state, country=country)

#     # Add edges for the paths between cities
#     for i in range(len(locations) - 1):
#         from_city = locations[i][3]
#         to_city = locations[i+1][3]
#         G.add_edge(from_city, to_city)

#     # Draw the graph
#     pos = {}
#     for i, node in enumerate(G.nodes()):
#         pos[node] = (i*10, i*10)
#     fig, ax = plt.subplots(figsize=(15,15))
#     ax.axis('off')
#     ax.tick_params(bottom=False, left=False)
#     nodes = nx.draw_networkx_nodes(G, pos, ax=ax, node_size=3000, node_color='red')
#     labels = nx.draw_networkx_labels(G, pos, font_size=16, ax=ax,horizontalalignment='center', verticalalignment='baseline' )

#     # Shift each node downwards by 0.1 units
#     pos_shifted = {node: (x, y-0.1) for node, (x, y) in pos.items()}

#     # Add dialog boxes to each node
#     node_labels = {}
#     for node in G.nodes():
#         label = f"State: {G.nodes[node]['state']}, Country: {G.nodes[node]['country']}"
#         node_labels[node] = label
#     nodes = nx.draw_networkx_nodes(G, pos_shifted, ax=ax, node_size=4010, node_color='skyblue',margins =0.1)
#     labels = nx.draw_networkx_labels(G, pos_shifted, node_labels, font_size=12, ax=ax,horizontalalignment='center', verticalalignment='top')

#     # Draw edges with weights
#     edges = nx.draw_networkx_edges(G, pos_shifted, ax=ax, edge_color='grey', width=2)
#     edge_labels = nx.draw_networkx_edge_labels(G, pos_shifted, font_size=10, ax=ax)

#     # Save the graph as HTML
#     html = mpld3.fig_to_html(fig)
#     with open(filename, 'w') as f:
#         f.write(html)


# !pip install pyvis
from pyvis import network as net 

def create_graph(locations, filename):
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

