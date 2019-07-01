import xml.etree.ElementTree as ET
from collections import defaultdict

tree = ET.parse('nlp.txt.xml')

triple_lst = []
for dependencies in tree.iter('dependencies'):  
    if dependencies.attrib['type'] == 'collapsed-dependencies':
        nsubj = defaultdict(str)
        dobj = defaultdict(str)
        for dep in dependencies.iter('dep'):
            governor = dep.find('governor').text
            dependent = dep.find('dependent').text
            if dep.attrib['type'] == 'nsubj':
                nsubj[governor] = dependent
            elif dep.attrib['type'] == 'dobj':
                dobj[governor] = dependent
        for pre, sub in nsubj.items():
            if dobj[pre] != '':
                triple_lst.append('{0}\t{1}\t{2}'.format(sub, pre, dobj[pre]))

with open('output58.txt', 'w') as f:
    for triple in triple_lst:
        f.write(triple + '\n')                  