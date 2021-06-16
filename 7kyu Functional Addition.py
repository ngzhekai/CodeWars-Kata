# --> Instruction <--
# Create a function add(n)/Add(n) which returns a function that always adds n to any number

# Note for Java: the return type and methods have not been provided to make it a bit more challenging.

# --> Instruction <--

# Example 1:
# add_one = add(1)
# add_one(3)  # 4

# Example 2:
# add_three = add(3)
# add_three(3) # 6

def add(n):
    def Add(x):
        return n+x
    return Add
