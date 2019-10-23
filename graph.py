import networkx as nx
import matplotlib.pyplot as plt


class GraphMaker:

    def __init__(self, list_of_edges=None):
        """
        Initialiezer for Graphs
        Uses Networkx plugin to construct graphs
        :param list_of_edges:
        """
        self.nx_graph = nx.Graph()
        self.nodes = self.nx_graph.nodes()
        self.edges_with_weight = []
        # If there is a pre-constructed list of edges available
        if list_of_edges is not None:
            self.sorted_edges = sorted(list_of_edges, key=lambda x: x[0])
            self.nx_graph.add_weighted_edges_from(list_of_edges)
        print(self.nodes)

    def add_edge(self, u, v, w):
        """
        Adds edge to the Graph
        :param u: First node of the edge
        :param v: Second node of the edge
        :param w: Weight of the Edge
        """

        if u not in self.nodes:
            self.nx_graph.add_node(u)
        if v not in self.nodes:
            self.nx_graph.add_node(v)
        self.nx_graph.add_edge(u, v, weight=w)
        self.edges_with_weight.append((u,v,w))

    def find(self,parent, i):
        """
        Find node in parent list
        :param parent: parent list
        :param i: node
        """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])


    def display(self,path=None,id=None):
        """
        Display Weighted graph using Matplotlib
        :param path: Minimum Spanning Tree
        """

        G=self.nx_graph
        pos = nx.spring_layout(G)  # positions for all nodes
        nx.draw(G,pos,node_color='k')
        # edges
        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
        if path is not None:
            nx.draw_networkx_edges(G, pos, edgelist=path, width=6, edge_color='r')
        else:
            nx.draw_networkx_edges(G,pos,width=1)
        # labels

        nx.draw_networkx_edge_labels(G, pos, font_size=10, font_family='sans-serif')


        plt.axis('off')
        plt.plot(weight=True, graph_border=True)
        if id is not None:
            path_to_jpg = 'graph' + str(id) + '.png'
            plt.savefig(path_to_jpg)
        plt.show()




