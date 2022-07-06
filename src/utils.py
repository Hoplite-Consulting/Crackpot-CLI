import re

def refine(l:list) -> list:
    retList = []
    for i in l:
        n = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        nn = n.sub('', i)
        retList.append(nn.strip())
    return retList

def makeDicts(l:list) -> list[dict]:
    retList = []
    tmp = []
    for i in l:
        t = []
        for o in i.split("  "): # Two spaces is important
            t.append(o)
        tmp.append(t)
    for i in tmp:
        try:
            s = i[-1].split("\\")
            u = s[1].split(":")[0]
            h = s[1].split(":")[3]
            retList.append({'user': u, 'hash': h, 'password': None})
        except IndexError:
            pass
    return retList

def cracked(path: str) -> list[dict]:
    retList = []
    with open(path, "r") as f:
        lines = f.readlines()
    for l in lines:
        hashPass = l.strip().split(":")
        retList.append({'hash': hashPass[0], 'password': hashPass[1]})
    return retList

def activeDirClean(path: str) -> list[dict]:
    with open(path, "r") as f:
        lines = f.readlines()
    retList = sorted(makeDicts(refine(lines)), key = lambda i: i['user'])
    return retList

def grepClean(path: str) -> list[dict]:
    with open(path, "r") as f:
        lines = f.readlines()
    keys = lines[0].strip().split("\t")
    users = []
    for l in lines[1:]:
        store = {}
        for var, key in zip(l.strip().split("\t"), keys):
            store[key] = var
        users.append(store)
    return users