# -*- coding: utf-8 -*-

import re
from lesson20 import getEngland

article_England = getEngland()
country_info = {}

kiso_pattern = r'^\{\{基礎情報(.*?)\}\}$'
kiso_match = re.findall(kiso_pattern, article_England, re.MULTILINE+re.DOTALL)

temp_pattern = r'^\|(.*?)\s=\s(.*?)\n'
temp_match = re.findall(temp_pattern, kiso_match[0], re.MULTILINE+re.DOTALL)

for (k, v) in temp_match:
    country_info[k] = v

for k, v in sorted(country_info.items(), key=lambda x: x[1]):
    print("key:{}".format(k))
    print("value:{}".format(v))
    print()


"""
# 正式国名だけうまく取り出せていない...
========
出力結果
========

key:夏時間
value:+1

key:面積大きさ
value:1 E11

key:人口大きさ
value:1 E7

key:水面積率
value:1.3%

key:GDP値元
value:1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>

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
value:2兆3162億<ref name="imf-statistics-gdp" />

key:GDP値MER
value:2兆4337億<ref name="imf-statistics-gdp" />

key:GDP/人
value:36,727<ref name="imf-statistics-gdp" />

key:国際電話番号
value:44

key:GDP順位MER
value:5

key:GDP順位
value:6

key:人口値
value:63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>

key:面積順位
value:76

key:注記
value:<references />

key:国旗画像
value:Flag of the United Kingdom.svg

key:ISO 3166-1
value:GB / GBR

key:通貨コード
value:GBP

key:位置画像
value:Location_UK_EU_Europe_001.svg

key:ccTLD
value:[[.uk]] / [[.gb]]<ref>使用は.ukに比べ圧倒的少数。</ref>

key:確立年月日2
value:[[1707年]]

key:確立年月日3
value:[[1801年]]

key:確立年月日4
value:[[1927年]]

key:確立年月日1
value:[[927年]]／[[843年]]

key:元首等肩書
value:[[イギリスの君主|女王]]

key:首相等肩書
value:[[イギリスの首相|首相]]

key:確立形態1
value:[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[連合法 (1707年)|1707年連合法]]まで）

key:元首等氏名
value:[[エリザベス2世]]

key:確立形態3
value:[[グレートブリテン及びアイルランド連合王国]]建国<br />（[[連合法 (1800年)|1800年連合法]]）

key:確立形態2
value:[[グレートブリテン王国]]建国<br />（[[連合法 (1707年)|1707年連合法]]）

key:通貨
value:[[スターリング・ポンド|UKポンド]] (&pound;)

key:首相等氏名
value:[[デーヴィッド・キャメロン]]

key:国章画像
value:[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]

key:首都
value:[[ロンドン]]

key:国歌
value:[[女王陛下万歳|神よ女王陛下を守り給え]]

key:公用語
value:[[英語]]（事実上）

key:公式国名
value:{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>

key:標語
value:{{lang|fr|Dieu et mon droit}}<br/>（[[フランス語]]:神と私の権利）

key:時間帯
value:±0

key:略名
value:イギリス

key:日本語国名
value:グレートブリテン及び北アイルランド連合王国

key:最大都市
value:ロンドン

key:建国形態
value:建国

key:確立形態4
value:現在の国号「'''グレートブリテン及び北アイルランド連合王国'''」に変更

key:国章リンク
value:（[[イギリスの国章|国章]]）

"""
