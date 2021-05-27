WIKI = 'https://en.wikipedia.org/wiki/'

import json

class Myrange:
    def __init__(self, path):
        self.index = -1
        with open(path, "r") as read_file:
            self.data = json.load(read_file)
            self.end = len(self.data)
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index >= self.end:
            raise StopIteration
        name = self.data[self.index]['name']['common']
        new_name = name.replace(' ', '_')
        return WIKI + new_name

if __name__ == '__main__':
    for i in Myrange('countries.json'):
        print(i)