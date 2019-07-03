import redis

def count_artists(country):
    counter = 0
    global r
    for name in r.scan_iter():
        areas = r.lrange(name, 0, -1)
        if country in areas:
            counter += 1
    return counter

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)

    print(count_artists(b'Japan')) # >>22554