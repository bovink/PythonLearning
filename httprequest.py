import requests
from json import JSONEncoder
import json


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class ResourceETag:

    def __init__(self, resourceId, eTag):
        self.resourceId = resourceId
        self.eTag = eTag


etags = []
if __name__ == '__main__':
    name = 'course10'
    file = open('download' + name + '.txt', 'r')
    a = file.readline()
    print(a)
    l = json.loads(a)
    for i in l:
        r = requests.head(i['downloadPath'])
        etags.append(ResourceETag(i['resourceId'], r.headers['ETag']))
        print('append')

    b = MyEncoder().encode(etags)
    f = open(name + 'etag.txt', 'w')
    f.write(b)
    print('over')
