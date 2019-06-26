# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ET
tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
for name in root.iter('word'):
    print(name.text)
