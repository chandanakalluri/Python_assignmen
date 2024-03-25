def mean_var_std():
    n, m = input().split()
    nInt = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))
    happiness = 0

    for i in nInt:
        if i in setA:
            happiness += 1
        if i in setB:
            happiness -= 1

    return happiness
#