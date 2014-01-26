def count(sequence, item):
    cnt = 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            cnt += 1
    return cnt

print count([[1,3],"xx",1,1], "xx")
