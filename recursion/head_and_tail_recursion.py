def calculate_head(n):
    if n > 0:
        calculate_head(n-1)
        k = n ** 2
        print(k)
        
def calculate_tail(n):
    if n > 0:
        k = n ** 2
        print(k)
        calculate_tail(n-1)
        
# calculate_head(4)
calculate_tail(4)