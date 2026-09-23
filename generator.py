def gen_fibonacci(n):
    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


# Test the generator
print("Fibonacci Sequence:")

for number in gen_fibonacci(10):
    print("Fibonacci number:", number)