def mean_var_std():
    import numpy as np
    n, m = map(int, input().split())
    l = []
    for i in range(n):
        ele = list(map(int, input().split()))
        l.append(ele)
    array = np.array(l)
    res=str(np.mean(array,axis=1))+"\n"+str(np.var(array,axis=0))+"\n"+str(round(np.std(array,axis=None),11))
    return res
