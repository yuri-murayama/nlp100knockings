import redis

def search(r,artist):
    area = r.lrange(artist,0,-1)
    if area != None:
        return area
    else:
        return 'None'

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)
    print('アーティスト名 : ',end = "")
    artist = input()
    print(search(r,artist))
