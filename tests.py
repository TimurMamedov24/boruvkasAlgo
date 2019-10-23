from boruvkas import BoruvkasAlgorithm
from graph import GraphMaker


def MST_problem_one():
    """
    Generate MST_problem_one
    :return:
    """
    g = GraphMaker()
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    A = BoruvkasAlgorithm(g)

    A.find_MST()
    print(A.cheapest_nodes)
    g.display()
    g.display(path=A.cheapest_nodes, id=1)
    print(A.cheapest_nodes)


def MST_problem_two():
    """
    Generate MST problem two
    :return:
    """
    B = GraphMaker()
    B.add_edge(0, 1, 25)
    B.add_edge(0, 2, 4)
    B.add_edge(0, 3, 10)
    B.add_edge(1, 3, 25)
    B.add_edge(2, 3, 10)
    B.add_edge(4, 2, 5)
    B.add_edge(4, 3, 6)
    B.add_edge(4, 1, 5)


    A = BoruvkasAlgorithm(B)

    A.find_MST()
    print(A.cheapest_nodes)
    B.display()
    B.display(path=A.cheapest_nodes, id=2)
    print(A.MST_weight)


if __name__ == "__main__":
    MST_problem_one()
    MST_problem_two()
