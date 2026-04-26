def fact(n):
    result = 1
    for i in fact(1,n+1):
        result *= i
        # print(fact(5))
    return result()