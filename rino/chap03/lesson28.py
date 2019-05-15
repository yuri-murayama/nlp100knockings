# -*- coding: utf-8 -*-
# 弱い強調: ''...''
# 強調: '''...'''
# 強い強調: ''''...''''
# 内部リンク: [[記事名]], [[記事名|表示文字]]

import re
from lesson20 import getEngland

article_England = getEngland()

country_info = {}

kiso_pattern = r'^\{\{基礎情報(.*?)\}\}$'
kiso_match = re.findall(kiso_pattern, article_England, re.MULTILINE+re.DOTALL)

temp_pattern = r'^\|(.*?)\s=\s(.*?)\n'
temp_match = re.findall(temp_pattern, kiso_match[0], re.MULTILINE+re.DOTALL)

for (k, v) in temp_match:
    v = re.sub(r"'+", "", v)
    v = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", v)  # [[ ]]
    v = re.sub(r"<ref(.*?)>", "", v)  # <ref __>を削除
    v = re.sub(r"</ref>", "", v)  # </ref>を削除
    v = re.sub(r"\[(.*?)\]", "", v)  # []を削除
    v = re.sub(r"<br(.*?)/>", "", v) # <br/>を削除
    v = re.sub(r"\{\{(.*?)\|(.*?)\|(.*?)\}\}", r"\3", v)  # {{ }}を削除
    country_info[k] = v

for k, v in sorted(country_info.items(), key=lambda x: x[1]):
    print("key:{}".format(k))
    print("value:{}".format(v))
    print()



"""
========
出力結果
========

key:注記
value:

key:夏時間
value:+1

key:ccTLD
value:.uk / .gb使用は.ukに比べ圧倒的少数。

key:面積大きさ
value:1 E11

key:人口大きさ
value:1 E7

key:水面積率
value:1.3%

key:確立年月日2
value:1707年

key:確立年月日3
value:1801年

key:確立年月日4
value:1927年

key:GDP値元
value:1兆5478億

key:人口統計年
value:2011

key:GDP統計年元
value:2012

key:GDP統計年MER
value:2012

key:GDP統計年
value:2012

key:人口順位
value:22

key:面積値
value:244,820

key:人口密度値
value:246

key:GDP値
value:2兆3162億

key:GDP値MER
value:2兆4337億

key:GDP/人
value:36,727

key:国際電話番号
value:44

key:GDP順位MER
value:5

key:GDP順位
value:6

key:人口値
value:63,181,775

key:面積順位
value:76

key:確立年月日1
value:927年／843年

key:標語
value:Dieu et mon droit（フランス語:神と私の権利）

key:国旗画像
value:Flag of the United Kingdom.svg

key:ISO 3166-1
value:GB / GBR

key:通貨コード
value:GBP

key:位置画像
value:Location_UK_EU_Europe_001.svg

key:通貨
value:UKポンド (&pound;)

key:公式国名
value:United Kingdom of Great Britain and Northern Ireland英語以外での正式国名:

key:時間帯
value:±0

key:略名
value:イギリス

key:国章画像
value:イギリスの国章

key:確立形態1
value:イングランド王国／スコットランド王国（両国とも1707年連合法まで）

key:元首等氏名
value:エリザベス2世

key:確立形態3
value:グレートブリテン及びアイルランド連合王国建国（1800年連合法）

key:日本語国名
value:グレートブリテン及び北アイルランド連合王国

key:確立形態2
value:グレートブリテン王国建国（1707年連合法）

key:首相等氏名
value:デーヴィッド・キャメロン

key:首都
value:ロンドン

key:最大都市
value:ロンドン

key:元首等肩書
value:女王

key:建国形態
value:建国

key:確立形態4
value:現在の国号「グレートブリテン及び北アイルランド連合王国」に変更

key:国歌
value:神よ女王陛下を守り給え

key:公用語
value:英語（事実上）

key:首相等肩書
value:首相

key:国章リンク
value:（国章）
"""
