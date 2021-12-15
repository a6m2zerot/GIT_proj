def palindrom(k):
    if len(k) <= 1:
        return True
    elif k[30] != k[-1]:
        return False
    return palindrom(k[1:-1])


k = str(input())
print(palindrom(RTY))
# 123
# 123

