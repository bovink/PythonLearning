import glob
import os
import hashlib
from json import JSONEncoder


def md5(fname):
    '''
    :param fname:
    :return: 获取md5
    '''
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class DownloadInfo:
    startId = 1
    courseId = 1

    def __init__(self, path: str):
        self.path = path
        self.storagePath = 'resource/courses/'
        self.downloadPath = 'http://ar.dolphinmedia.cn/dolphinenglishresource/pearsonprimer/'
        self.initInfo()

    def initInfo(self):
        index = self.path.rfind('/')
        parentPath = self.path[:index + 1]
        self.courseId = DownloadInfo.courseId
        self.storagePath += parentPath
        self.downloadPath += self.path
        self.md5 = md5(self.path)
        self.resourceVersion = 1
        self.resourceId = DownloadInfo.startId
        DownloadInfo.startId += 1
        self.fileName = self.path[index + 1:]
        del self.path
        pass


infos = []


def findFoldWithFile(rootPath):
    allContent = '/*'
    for path in glob.glob(rootPath + allContent):
        if os.path.isdir(path):
            findFoldWithFile(path)
        elif os.path.isfile(path):
            getInfo(path)


def getInfo(filePath):
    a = DownloadInfo(filePath)

    infos.append(a)
    print(a.startId)


if __name__ == '__main__':
    rootPath = 'course10'
    DownloadInfo.courseId = 10
    DownloadInfo.startId = 599
    findFoldWithFile(rootPath)
    a = MyEncoder().encode(infos)
    f = open('download' + rootPath + '.txt', 'w')
    f.write(a)
