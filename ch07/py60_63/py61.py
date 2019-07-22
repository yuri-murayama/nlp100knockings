import redis

def num_key():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    v = r.get('The Silhouettes').decode()
    print(v)
    v = r.get('The Wanderers').decode()
    print(v)
    v = r.get('Pierre F. Brault').decode()
    print(v)


def main():
    num_key()

if __name__ == '__main__':
    main()
