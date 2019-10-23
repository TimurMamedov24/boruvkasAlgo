from graph import GraphMaker


class BoruvkasAlgorithm:

    def __init__(self, graph):
        """
        Constructor For Boruvkas Algorithm class
        :param graph: Instance of the class graph
        """
        self.graph = graph
        self.graph_edges = self.graph.edges_with_weight # list of edges
        self.V = len(self.graph.nodes) # number of nodes
        self.cheapest = [-1] * self.V # cheapest edges
        self.cheapest_nodes = [] #cheapest path
        self.MST_weight = 0 # weight of the tree
        self.parents = [] # place holder for parents
        self.rank = [] # rank of nodes

        print(self.graph_edges)

    def find_cheapest(self):
        """
        First part of Boruvka's algortihtm
        Finds cheapest roots for all nodes in the graph
        """
        a = self.graph.edges_with_weight
        for i in range(len(a)):
            u, v, w = a[i]
            set1 = u
            set2 = v

            # Fill the cheapest set
            # Fill if empty, or change if smaller weight
            if set1 != set2:

                if self.cheapest[set1] == -1 or self.cheapest[set1][2] > w:
                    self.cheapest[set1] = [u, v, w]

                if self.cheapest[set2] == -1 or self.cheapest[set2][2] > w:
                    self.cheapest[set2] = [u, v, w]

    def union(self,x, y):
        """
        Join two nodes in to a group
        Increase the rank of the first node
        :param x: node
        :param y: node
        :return:
        """

        xroot = self.graph.find(self.parents, x)
        yroot = self.graph.find(self.parents, y)

        # Group higher rank tree with a smaller one
        if self.rank[xroot] < self.rank[yroot]:
            self.parents[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parents[yroot] = xroot

        # If ranks are same, then make one as root and increment
        # its rank by one
        else:
            self.parents[yroot] = xroot
            self.rank[xroot] += 1

    def find_MST(self):
        """
        Second part of Boruvka's Algorithm
        :return:
        """
        numTrees = self.V
        MSTweight = 0

        for n in range(self.V):
            self.parents.append(n)
            self.rank.append(0)

        while numTrees > 1:
            self.find_cheapest()
            for node in range(self.V):
                if self.cheapest[node] != -1:
                    u, v, w = self.cheapest[node]
                    set1 = self.graph.find(self.parents, u)
                    set2 = self.graph.find(self.parents, v)
                    print(set1, set2)
                    if set1 != set2:
                        MSTweight += w
                        self.union(set1, set2)
                        print("Edge %d-%d with weight %d included in MST" % (u, v, w))
                        numTrees = numTrees - 1

        # reset cheapest array
        self.cheapest_nodes = self.cheapest
        self.cheapest = [-1] * self.V
        self.MST_weight = MSTweight
        return MSTweight
