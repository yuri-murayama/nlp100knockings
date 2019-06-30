# -*- coding: utf-8 -*-

from xml.etree import ElementTree

def getChunk(elem, sentence_id, start_id, end_id):
    """
    tree, 文章id、スタートid、エンドidを受け取ったら、
    その文節のテキストを返す関数
    """
    text = ""
    for sentence in elem.iter('sentence'):
        if sentence.attrib != {}:
            if int(sentence.attrib['id']) == sentence_id:
                for token in sentence.iter('token'):
                    token_id = int(token.attrib['id'])
                    if token_id >= start_id and token_id < end_id:
                        text += token.find('word').text
                        if token_id + 1 != end_id:
                            text += " "
    return text

def getMentionList(elem):
    """
    xmlのtreeを受け取って、
    [{'representative': 'PARRY , Racter , and Jabberwacky', 'sentence': 16, 'start': 10, 'end': 11},
    {'representative': 'hand-written rules', 'sentence': 39, 'start': 23, 'end': 25},...
    という形のMention辞書のリストを作成する関数
    """
    # 参照のリストを作成する
    mention_dict_list = []
    for coreference in elem.iter('coreference'):
        representative_text = ""
        for mention in coreference.iter('mention'):

            if mention.attrib != {}:
                # 代表参照
                representative_text = getChunk(elem,
                                               int(mention.find('sentence').text),
                                               int(mention.find('start').text),
                                               int(mention.find('end').text))
            else:
                mention_dict = {}
                mention_dict['representative'] = representative_text
                mention_dict['sentence'] = int(mention.find('sentence').text)
                mention_dict['start'] = int(mention.find('start').text)
                mention_dict['end'] = int(mention.find('end').text)
                mention_dict_list.append(mention_dict)

    # リスト内の重複を削除
    mention_dict_list_real = []
    for i in range(len(mention_dict_list)):
        if mention_dict_list[i] not in mention_dict_list[i+1:]:
            mention_dict_list_real.append(mention_dict_list[i])

    return mention_dict_list_real

if __name__ == "__main__":
    INPUT_XML_PATH = "./nlp2.txt.xml"
    OUTPUT_TEXT_PATH = "./output56.txt"
    fw = open(OUTPUT_TEXT_PATH, "w")

    # XML ファイルから ElementTree オブジェクトを生成
    tree = ElementTree.parse(INPUT_XML_PATH)

    # 先頭要素を表す Element オブジェクトを取得
    elem = tree.getroot()


    # すべての文章を繋げる
    all_sentence = []
    for sentence in elem.iter('sentence'):
        if sentence.attrib != {}:
            sentence_list = []
            for token in sentence.iter('token'):
                sentence_list.append(token.find('word').text)
            all_sentence.append(sentence_list)

    mention_dict_list = getMentionList(elem)

    # 書き換え
    all_sentence_tmp = all_sentence
    for mention_dic in mention_dict_list:
        # chunkの始まり
        all_sentence_tmp[mention_dic['sentence']-1][mention_dic['start']-1] = "「{} ({}".format(mention_dic['representative'],
                                                                                                all_sentence[mention_dic['sentence']-1][mention_dic['start']-1])

        # chunkの終わり
        all_sentence_tmp[mention_dic['sentence']-1][mention_dic['end']-2] = "{})」".format(all_sentence[mention_dic['sentence']-1][mention_dic['end']-2])

    # 出力
    for sen in all_sentence_tmp:
        fw.write(" ".join(sen) + "\n\n")
