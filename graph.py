import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO

def generate_graph(data):
    # Initialize a directed graph and add edges based on the provided data
    G = nx.DiGraph()

    # Add edges directly from the data dictionary
    for course, prerequisites in data.items():
        G.add_edges_from((prereq, course) for prereq in prerequisites)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    pos = nx.planar_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, 
            font_size=10, font_weight='bold', arrows=True, arrowstyle='->', arrowsize=15)

    # Save the figure to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the plot to free memory
    img.seek(0)  # Move to the beginning of the BytesIO object
    return img
