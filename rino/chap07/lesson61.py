# -*- coding: utf-8 -*-

import plyvel

OUTPUT_DB_PATH = 'lesson60.ldb'
a_artist = "Neikka RPM"

db = plyvel.DB(OUTPUT_DB_PATH, create_if_missing=True)
an_area = db.get(a_artist.encode())
print(an_area)
