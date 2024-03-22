def second_max():
    arr = input().split()
    unique=[]
    for i in arr:
        if i not in unique:
            unique.append(i)
    #uniq=sorted(unique)
    max1=int(unique[0])
    max2=int(unique[0])
    for j in unique:
        if int(j)>max1:
            max2=max1
            max1=int(j)
        elif int(j)>max2:
            max2=int(j)
    return max2
print(second_max())



