import time

def calculate(n):
    if n > 0:
        calculate(n - 1)
        k = n ** 2
        # print(k)
        calculate(n - 1)

# Start time
start_time = time.time()

# Function call
calculate(50)

# End time
end_time = time.time()

# Total execution time
print(f"\nTotal time taken: {end_time - start_time:.4f} seconds")
