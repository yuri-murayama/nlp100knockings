# -*- coding: utf-8 -*-

from xml.etree import ElementTree

def getNPword(parse_part):
    """
    NPが現れたあとのS式全体を受け取ってきて、
    NPの部分の文字列を返す関数
    """
    np_text = ""
    depth = 1
    i = 0
    is_pos = False

    while depth != 0:
        if parse_part[i] == "(":
            is_pos = True
            depth += 1

        elif parse_part[i] == ")":
            depth -= 1

        elif parse_part[i] == " ":
            is_pos = False
            np_text += parse_part[i]

        else:
            if not(is_pos):
                np_text += parse_part[i]

        i += 1

    # 空白とか綺麗にする
    np_text_list = []
    for np_t in np_text.split(" "):
        if np_t != '':
            np_text_list.append(np_t)

    np_text = " ".join(np_text_list)

    return np_text

def getNPwordFromS(parse):
    """
    S式を受け取って、NPの文字列を返す関数
    """
    i = 0
    is_pos = False
    is_NP = False
    pos = ""
    chunk = ""
    chunk_list = []
    while i < len(parse):

        if is_NP:
            chunk += parse[i]

        if parse[i] == "(":
            if pos == "NP":
                is_NP = True
                chunk_list.append(getNPword(parse[i:]))

            is_pos = True
            pos = ""

        elif parse[i] == ")":
            pass

        elif parse[i] == " ":
            is_pos = False

        else:
            if is_pos:
                pos += parse[i]

        i += 1

    return chunk_list

if __name__ == '__main__':
    INPUT_XML_PATH = "./nlp2.txt.xml"
    OUTPUT_TEXT_PATH = "./output59.txt"
    fw = open(OUTPUT_TEXT_PATH, "w")

    # XML ファイルから ElementTree オブジェクトを生成
    tree = ElementTree.parse(INPUT_XML_PATH)

    # 先頭要素を表す Element オブジェクトを取得
    elem = tree.getroot()

    for sentence in elem.iter('sentence'):

        if sentence.attrib == {}:
            continue

        fw.write("====== sentence_id:{} ======\n".format(sentence.attrib['id']))
        parse = sentence.find('parse').text.strip()

        np_word_list = getNPwordFromS(parse)

        for np_word in np_word_list:
            fw.write(np_word + "\n")

        fw.write("\n")
