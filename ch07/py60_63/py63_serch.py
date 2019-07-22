import json
import redis

def print_tag(r, name):
    v = r.get(name)
    if v != None:
        print('NAME:\t' + name)
        tags = json.loads(v.decode())
        for tag in tags:
            print("{}\t{}".format(tag['value'], tag['count']))
    #print('\n')

def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    print_tag(r, 'George Winston')
    print_tag(r, 'Mariah Carey')
    print_tag(r, 'Pierre F. Brault')

if __name__ == '__main__':
    main()
