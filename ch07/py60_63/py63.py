import json
import redis

def num_k():
    with open('artist.json', 'r', encoding='utf8') as f:
        for line in f:
            j = json.loads(line)
            if 'tags' in j:
                yield j['name'], json.dumps(j['tags'])

def register():
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    r.flushdb()

    for k, v in num_k():
        r.set(k, v)
        
    r.save()

def main():
    register()

if __name__ == '__main__':
    main()
