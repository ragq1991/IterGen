import hashlib

def gen(path):
    with open(path, "r") as data:
        end = sum(1 for line in data)
        data.seek(0)
        for i in range(0, end):
            if i > end:
                raise StopIteration
            hash = hashlib.md5(data.read(i).encode())
            yield hash.hexdigest()


if __name__ == '__main__':
    for i in gen('countries.txt'):
        print(i)
