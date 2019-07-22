import xml.etree.ElementTree as ET
import os
import pydot

class Dependencies:
    def __init__(self, filepath):
        x = ET.parse(filepath)
        root = x.getroot()
        self.sentences = root.find('document/sentences')
        self.coreference = root.find('document/coreference')

    def num(self):
        for i in self.coreference:
            yield i

    @staticmethod
    def toDot(deps):
        edges = []
        for dep in deps:
            governor = dep.find('governor')
            dependent = dep.find('dependent')
            if dependent.text != '.' and dependent.text != ',':
                edges.append((governor.text, dependent.text))
        return edges

    def getDependence(self, sentenceId):
        strid = str(sentenceId)
        sentences = self.sentences.find("sentence[@id='" + strid + "']")
        deps = sentences.find('dependencies[@type="collapsed-dependencies"]')
        return self.toDot(deps)

    def enumDependencies(self):
        dependencies = self.sentences.findall('sentence/dependencies[@type="collapsed-dependencies"]')
        for deps in dependencies:
            yield self.toDot(deps)

    @staticmethod
    def toGraph(dot, filepath):
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

        graph = pydot.Dot(graph_type='digraph')
        graph.set_node_defaults(fontname='Meiryo UI', fontsize='10')

        for s, t in dot:
            graph.add_edge(pydot.Edge(s, t))
        graph.write_png(filepath)

def main():
    y = Dependencies('nlp.txt.xml')
    # てきとうに指定
    sentenceId = 5
    z = y.getDependence(sentenceId)
    y.toGraph(z, "./output57/py57_{}.png".format(sentenceId))

if __name__ == '__main__':
    main()
