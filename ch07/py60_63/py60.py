import redis
import json

def num_k():
    with open('artist.json', 'r', encoding='utf8') as f:
        for line in f:
            j = json.loads(line)
            if 'area' in j:
                yield j['name'], j['area']

def register():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.flushdb()
    for k, v in num_k():
        r.set(k, v)
    r.save()

def main():
    register()

if __name__ == '__main__':
    main()
