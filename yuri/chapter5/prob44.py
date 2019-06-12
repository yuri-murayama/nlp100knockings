from prob41 import load_neko
from prob42 import depend
import pydot

if __name__ == '__main__':
    text = load_neko()
    lst = depend(text[7])

    G = pydot.Dot(graph_type='digraph')
    G.set_node_defaults(shape='circle')
    for l in lst:
        G.add_edge(pydot.Edge(l[0], l[1]))
    G.write_png('dependency_tree.png')