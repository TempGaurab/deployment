import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
from networkx.drawing.nx_pydot import graphviz_layout

def generate_graph(data):
    # Initialize a directed graph
    G = nx.DiGraph()

    # Add edges based on the provided data
    for course, prerequisites in data.items():
        for prereq in prerequisites:
            G.add_edge(prereq, course)

    # Draw the graph
    plt.figure(figsize=(12, 10))
    
    # Use graphviz_layout with "twopi" for hierarchical layout
    pos = graphviz_layout(G, prog="circo")
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue')
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

    plt.title("Course Prerequisites Graph (Hierarchical Layout)")
    plt.axis('off')  # Turn off axis

    # Save the figure to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png', dpi=300, bbox_inches='tight')
    plt.close()  # Close the plot to free memory
    img.seek(0)  # Move to the beginning of the BytesIO object
    return img
