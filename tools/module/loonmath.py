def fact(n):
    ret = 1
    for i in range(2, n+1):
        ret *= i
    return ret

def C(n, k):
    if n < k:
        return 0
    ret = 1
    for i in range(1, k+1):
        ret =ret * (n-i+1)/i
    return ret

# Stirling number of the 2nd kind
def Stirling_2(n, k):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0 or n < k:
        return 0
    if n == k or k == 1:
        return 1
    return Stirling_2(n-1, k-1) + Stirling_2(n-1, k) * k

