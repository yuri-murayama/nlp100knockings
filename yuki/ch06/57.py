#Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
#可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
from graphviz import Digraph
from xml.etree import ElementTree
import pydot

tree_parse = ElementTree.parse('nlp2.txt.xml')

governor_list = []
dependent_list = []


for j ,dependencies in enumerate(tree_parse.iter('dependencies')):
    if dependencies.get("type") == 'collapsed-dependencies':
        for governor in dependencies.iter('governor'):
            governor_list.append(governor.text)
        for dependent in dependencies.iter('dependent'):
            dependent_list.append(dependent.text)
    if len(governor_list) >0 :
        G = Digraph(format='png')
        G.attr('node', shape='circle')
        for i in range(len(governor_list)):
            G.edge(governor_list[i], dependent_list[i])
        G.render(str(j))
        governor_list = []
        dependent_list = []
