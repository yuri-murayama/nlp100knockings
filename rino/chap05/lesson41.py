# -*- coding: utf-8 -*-

from lesson40 import Morph

class Chunk:
    def __init__(self, lines):
        line = lines.split("\n")
        self.index = line[0].split(" ")[0]
        self.dst = int(line[0].split(" ")[1].rstrip('D'))
        self.morphs = []
        self.srcs = []

        for word_info in line[1:]:
            if word_info == "":
                continue

            neko_morph = Morph(word_info)
            self.morphs.append(neko_morph)

def getChunkCabocha(contents):
    """
    CaboChaの解析結果から1文ごとのChunkオブジェクトのリストを取得する
    係り元文節インデックス番号のリストは空のまま

    args:
     - contents: CaboChaの解析結果  # strings

    returns:
     - cabocha_chunk_list:  # Chunkオブジェクトのリスト
    """

    cabocha_chunk_list = []
    sentence_info_list = contents.split("EOS\n")

    for sentence in sentence_info_list:
        chunk_sentence_list = []
        chunk_list = sentence.split("* ")[1:]

        for lines in chunk_list:
            c = Chunk(lines)
            chunk_sentence_list.append(c)

        cabocha_chunk_list.append(chunk_sentence_list)

    cabocha_chunk_list = addChunkSrcs(cabocha_chunk_list)

    return cabocha_chunk_list

def addChunkSrcs(cabocha_chunk_list):
    """
    Chunkオブジェクトのリストの
    係り元文節インデックス番号(srcs)を追加する

    args:
     - cabocha_chunk_list: # Chunkオブジェクトのリスト(srcs なし)

    returns:
     - cabocha_chunk_list:  # Chunkオブジェクトのリスト(srcs あり)
    """

    for sen in cabocha_chunk_list:
        for i in range(len(sen)):
            for chu in sen:
                if int(chu.dst) == i:
                    sen[i].srcs.append(int(chu.index))

    return cabocha_chunk_list

def getNekoChunk():

    CABOCHA_PATH = "./neko.txt.cabocha"

    cabocha_data = open(CABOCHA_PATH, "r")
    contents = cabocha_data.read()
    neko_chunk = getChunkCabocha(contents)
    cabocha_data.close()

    return neko_chunk

if __name__ == "__main__":
    neko_list = getNekoChunk()

    for chunk_info in neko_list[7]:
        for word_info in chunk_info.morphs:
            print(word_info.surface, end=" ")
        print("index:{}, dst:{}".format(chunk_info.index, chunk_info.dst))


"""
========
出力結果
========

吾輩 は index:0, dst:5
ここ で index:1, dst:2
始め て index:2, dst:3
人間 という index:3, dst:4
もの を index:4, dst:5
見 た 。 index:5, dst:-1

"""
