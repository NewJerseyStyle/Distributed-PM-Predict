from tinydb import TinyDB, Query
import numpy as np

def weighted_mean(x):
    return sum([np.prod(y) for y in x])/sum([np.prod(y, where=[True, False, True]) for y in x])


def weighted_median(x):
    y = [np.prod(y, where=[True, False, True]) for y in x]
    z = sum(y) / 2
    while sum(y) > z:
        y.pop()
    return x[len(y)][1]


def takeSecond(elem):
    return elem[1]


def run(k=5):
    with TinyDB('db.json') as db:
        ds_db = db.table('qips')
        db.drop_table('ranks')
        rs_db = db.table('ranks')
        results = []
        for ds in ds_db:
            l = []
            for i, p, s in zip(ds['i'], ds['p'], ds['s']):
                l.append([i, p, s])
            l.sort(key=takeSecond)
            x = np.array(l)
            results.append((ds['q'],
                            ((weighted_mean(x) + weighted_median(x)) / 2 +
                              max(weighted_mean(x), weighted_median(x))),
                            max(weighted_mean(x), weighted_median(x))
                            ))
        results.sort(key=takeSecond)
        topk = list(reversed(results[-k:]))
        for name, score in topk:
            rs_db.insert({'name': name,
                'a': weighted_mean(x),
                'b': weighted_median(x)})
    return topk
