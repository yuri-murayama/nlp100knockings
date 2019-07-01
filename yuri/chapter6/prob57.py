import xml.etree.ElementTree as ET
import pydot

tree = ET.parse('nlp.txt.xml')

sentences = []
for dependencies in tree.iter('dependencies'):   
    if dependencies.attrib['type'] == 'collapsed-dependencies': 
        sentence = []      
        for dep in dependencies.iter('dep'):
            governor = ' ' + dep.find('governor').text # ?
            dependent = ' ' + dep.find('dependent').text
            sentence.append((governor, dependent))
        sentences.append(sentence)

G = pydot.Dot(graph_type='digraph')
G.set_node_defaults(shape='circle')
for pair in sentences[0]:
    G.add_edge(pydot.Edge(pair[0], pair[1]))
G.write_png('output57.png')