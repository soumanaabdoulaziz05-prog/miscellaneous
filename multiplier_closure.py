def make_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


# Create two multiplier functions
times3 = make_multiplier(3)
times10 = make_multiplier(10)


# Test the functions
print("7 multiplied by 3:", times3(7))
print("7 multiplied by 10:", times10(7))