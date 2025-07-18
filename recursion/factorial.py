def fact_rec(n):
    if n == 0:
        return 1

    return fact_rec(n-1) * n

num = input('Enter Number: ')
n = int(num)
print(fact_rec(n))