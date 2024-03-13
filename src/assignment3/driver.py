from Python_assignmen.src.assignment3.util import mutate_string
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
