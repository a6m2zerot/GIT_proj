def palindrom(k):
    if len(k) <= 1:
        return True
    elif k[0] != k[-1]:
        return False
    return palindrom(k[1:-1])


k = str(input())
print(palindrom(k))

