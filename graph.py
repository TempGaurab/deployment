import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
from networkx.drawing.nx_agraph import graphviz_layout

def generate_graph(data):
    # Initialize a directed graph
    G = nx.DiGraph()

    # Add edges based on the provided data
    for course, prerequisites in data.items():
        for prereq in prerequisites:
            G.add_edge(prereq, course)

    # Draw the graph
    nx.nx_agraph.write_dot(G,'test.dot')
    plt.figure(figsize=(10, 8))
    pos=graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
    plt.title("Course Prerequisites Graph")

    # Save the figure to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the plot to free memory
    img.seek(0)  # Move to the beginning of the BytesIO object
    return img