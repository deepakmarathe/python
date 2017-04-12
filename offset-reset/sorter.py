import glob, os


def getIndex(file):
    return file.split('/')[-1].split('.')[0]


def getTimeIndexMap(directory, t_c):
    files = glob.glob(dataset_path+"*.index")
    files.sort(key=os.path.getmtime)
    # print(files)
    map = {}
    t = os.path.getmtime(files[0])
    for f in files[1:]:
        i = getIndex(f)
        map[t] = i
        t = os.path.getmtime(f)

    return map


def getoffset(directory, t_c):
    files = glob.glob(directory+"*.index")
    files.sort(key=os.path.getmtime)
    # print(files)

    t = os.path.getmtime(files[0])
    a = []
    for f in files[1:]:
        i = getIndex(f)
        a.append((t, i))
        t = os.path.getmtime(f)

    # print(a)

    prev = a[0]
    for t in a[1:]:
        if t[0] < t_c:
            prev = t

    # print(prev)

    return prev[1]


dataset_path='/Users/deepakmarathe/workspace/python/a-1/'
offset = getoffset(dataset_path, 1491996450)
print(offset)