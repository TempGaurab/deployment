import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from io import BytesIO

def generate_graph(data):
    # Initialize a directed graph and add edges based on the provided data
    G = nx.DiGraph()

    # Add edges directly from the data dictionary
    for course, prerequisites in data.items():
        G.add_edges_from((prereq, course) for prereq in prerequisites)

    # Assign a 'layer' attribute to each node based on the number of prerequisites
    for course, prerequisites in data.items():
        G.nodes[course]['subset'] = len(prerequisites)
        for prereq in prerequisites:
            G.nodes[prereq]['subset'] = G.nodes[prereq].get('subset', 0)

    # Determine the main node (the first course in the data dictionary)
    main_node = list(data.keys())[0]

    # Compute the shortest path length from the main node to every other node
    depth = nx.single_source_shortest_path_length(G, main_node)

    # Normalize the depth values for color scaling
    max_depth = max(depth.values())
    
    # Create a color map ranging from dark to light blue
    cmap = LinearSegmentedColormap.from_list("blues_gradient", ["#003366", "#6699CC", "#99CCFF"])
    
    # Assign colors based on the depth of each node
    node_colors = [cmap(depth[node] / max_depth) for node in G.nodes]

    # Draw the graph
    plt.figure(figsize=(10, 8))
    
    # Generate the multipartite layout with the top-to-bottom orientation
    pos = nx.multipartite_layout(G, subset_key='subset')
    
    # Adjust the positions to flip the graph to a top-to-bottom layout
    pos = {node: (-x, y) for node, (x, y) in pos.items()}

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, 
            font_size=10, font_weight='bold', arrows=True, arrowstyle='->', arrowsize=15)
    
    # Save the figure to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the plot to free memory
    img.seek(0)  # Move to the beginning of the BytesIO object
    return img
