import redis

def search_area(name):
    global r
    areas = r.lrange(name, 0, -1)
    if areas != []:
        print(areas)
    else:
        print('そのようなアーティストはデータベース内に存在しません')

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)

    search_area('Richard Benson') # >>[b'None', b'United Kingdom', b'Italy', b'None']
    search_area('大友') # >>そのようなアーティストはデータベース内に存在しません