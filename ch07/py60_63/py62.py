import redis

def count_ja():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    keys = r.scan_iter()
    count = 0
    
    for key in keys:
        v = r.get(key)
        if v == b'Japan':
            count = count + 1
    print(count)

def main():
    count_ja()

if __name__ == '__main__':
    main()
