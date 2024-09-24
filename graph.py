import networkx as nx
import matplotlib.pyplot as plt
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

    # Draw the graph
    plt.figure(figsize=(10, 8))
    
    # Generate the multipartite layout with the top-to-bottom orientation
    pos = nx.multipartite_layout(G, subset_key='subset')
    
    # Adjust the positions to flip the graph to a top-to-bottom layout
    pos = {node: (-x, y) for node, (x, y) in pos.items()}

    # Set node colors: red for the main node, lightblue for others
    node_colors = ['red' if node == main_node else 'lightblue' for node in G.nodes]

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, 
            font_size=10, font_weight='bold', arrows=True, arrowstyle='->', arrowsize=15)
    
    # Save the figure to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the plot to free memory
    img.seek(0)  # Move to the beginning of the BytesIO object
    return img
