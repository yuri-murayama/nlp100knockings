import xml.etree.ElementTree as ET

class Dependency:
    def __init__(self, dep):
        self.type = dep.attrib['type']
        self.governor_ix = dep.find('governor').attrib['idx']
        self.governor_text = dep.find('governor').text
        self.dependent_ix = dep.find('dependent').attrib['idx']
        self.dependent_text = dep.find('dependent').text

class Dependency2:
    def __init__(self, filepath):
        xdoc = ET.parse(filepath)
        root = xdoc.getroot()
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
        return deps

    def num_d(self):
        dependencies = self.sentences.findall('sentence/dependencies[@type="collapsed-dependencies"]')
        for deps in dependencies:
            yield deps

    @staticmethod
    def toList(deps):
        lst = []
        for dep in deps:
            lst.append(Dependency(dep))
        return lst


    def extractSVO(self, lst):
        subjs = self.findSubj(lst)
        for subj in subjs:
            objs = self.finObjs(lst, subj)
            for obj in objs:
                yield (subj.dependent_text, subj.governor_text, obj.dependent_text)

    @staticmethod
    def findSubj(lst):
        return filter(lambda x: x.type == 'nsubj', lst)

    @staticmethod
    def finObjs(lst, subj):
        filterd = filter(lambda x: x.governor_ix == subj.governor_ix, lst)
        return filter(lambda x: x.type == 'dobj', filterd)

def main():
    cd = Dependency2('nlp.txt.xml')
    with open('py58.txt', 'w', encoding='utf8') as w:
        for deps in cd.num_d():
            nodes = cd.toList(deps)
            for s, v, o in cd.extractSVO(nodes):
                w.write('{}\t{}\t{}\n'.format(s, v, o))

if __name__ == '__main__':
    main()
