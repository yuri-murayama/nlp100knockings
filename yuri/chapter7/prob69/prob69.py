from pymongo import MongoClient

def reshape1(field, artist_dict, post):
    if field in post:
        artist_dict[field] = post[field]
    else:
        artist_dict[field] = '該当なし'

def reshape2(field, artist_dict, post):
    if field in post and 'year' in post[field]:
        artist_dict[field] = post[field]['year']
    else:
        artist_dict[field] = '該当なし'

def reshape3(field, field0, artist_dict, post):
    if field in post:
        field0_lst = [d[field0] for d in post[field]]
        artist_dict[field] = ', '.join(field0_lst)
    else:
        artist_dict[field] = '該当なし'

def reshape(post): # 画面表示用に整形
    artist_dict = {}
    reshape1('name', artist_dict, post)
    reshape3('aliases', 'name', artist_dict, post)
    reshape1('area', artist_dict, post)
    reshape2('begin', artist_dict, post)
    reshape2('end', artist_dict, post)
    reshape3('tags', 'value', artist_dict, post)

    if 'rating' in post:
        artist_dict['rating'] = post['rating']['value']
    else:
        artist_dict['rating'] = 0

    return artist_dict

def find_artists(name, area, tag): 
    client = MongoClient()
    db = client.artist_db
    collection = db.artist_collection

    condition_lst = []

    if name != '':
        condition_lst.append({'$or': [{'name': name}, {'aliases.name': name}]})
    if area != '':
        condition_lst.append({'area': area})
    if tag != '':
        condition_lst.append({'tags.value': tag})

    if len(condition_lst) == 3:
        condition = {'$and': [condition_lst[0], condition_lst[1], condition_lst[2]]}
    elif len(condition_lst) == 2:
        condition = {'$and': [condition_lst[0], condition_lst[1]]}
    else:
        condition = condition_lst[0]

    posts = []
    for post in collection.find(condition).sort('rating.value', -1):
        posts.append(reshape(post))

    return posts