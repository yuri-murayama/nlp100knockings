def fopen():
    with open('UK.txt', 'r') as f:
        return ''.join(f)

if __name__ == '__main__':
    t = fopen()
    l = [line for line in t.split('\n') if 'Category' in line]
    print(l)