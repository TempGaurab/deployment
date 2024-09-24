import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO

def generate_graph(data):
    # Initialize a directed graph
    G = nx.DiGraph()

    # Add edges based on the provided data
    for course, prerequisites in data.items():
        for prereq in prerequisites:
            G.add_edge(prereq, course)
    # Print the contents of G (edges)
    edges = list(G.edges())
    G = nx.DiGraph()
    G.add_edges_from(edges)
    # Draw the graph
    plt.figure(figsize=(10, 8))
    pos = nx.nx_pydot.graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, 
        font_size=10, font_weight='bold', arrows=True, arrowstyle='->', arrowsize=15)
    # Save the figure to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the plot to free memory
    img.seek(0)  # Move to the beginning of the BytesIO object
    return img