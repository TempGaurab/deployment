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

    # Ensure that all courses are added to the graph, even if they have no prerequisites
    for course in data.keys():
        if course not in G:
            G.add_node(course, subset=0)

    keys = list(data.keys())
    main_node = keys[0] if len(keys) > 0 else ""

    # Define the next badge of prerequisites
    next_badge = set(G.predecessors(main_node))  # This represents the direct prerequisites for the main node

    # Define node colors with the next badge being a different color (e.g., 'green')
    node_colors = [
        'orange' if node == main_node else 
        'green' if node in next_badge else 
        '#D6BF73' if node in G.predecessors(next_badge) else 
        '#add8e6' 
        for node in G.nodes
    ]

    # Generate the multipartite layout with the top-to-bottom orientation
    pos = nx.multipartite_layout(G, subset_key='subset', align='horizontal')

    # Draw the graph
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, 
            font_size=10, font_weight='bold', arrows=True, arrowstyle='->', arrowsize=15)

    # Save the figure to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()  # Close the plot to free memory
    img.seek(0)  # Move to the beginning of the BytesIO object
    return img
g