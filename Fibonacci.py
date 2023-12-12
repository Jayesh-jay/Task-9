from functools import reduce

# Define a lambda function that generates a Fibonacci series up to n elements
# use the reduce function along with a lambda expression 
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

# Print the Fibonacci series up to 50 elements
print("fibonacci series:",fib_series(50))