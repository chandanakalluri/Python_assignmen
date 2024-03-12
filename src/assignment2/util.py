def second_la():
    n = int(input())
    arr = map(int, input().split())
    return sorted(set(arr))[-2]



