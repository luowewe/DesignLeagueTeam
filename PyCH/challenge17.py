def is_power(a, b):
    # Base case: if a is less than b, it cannot be a power of b.
    if a < b:
        return False  # If a is smaller than b, return False because it can't be a power of b.

    # Base case: if a is exactly equal to b, it is a power of b (b^1).
    if a == b:
        return True  # If a equals b, return True, as b^1 = b.

    # Recursive case: check if a is divisible by b.
    if a % b == 0:  # If a is divisible by b (no remainder),
        return is_power(a // b, b)  # Recursively check if the quotient (a // b) is a power of b.

    # If a is not divisible by b, then it is not a power of b.
    return False  # If a is not divisible by b, return False, as it's not a power of b.

# Test cases
print(is_power(16, 2))  # Expected: True, since 16 = 2^4. It divides by 2, then 8, 4, and finally 2.
print(is_power(27, 3))  # Expected: True, since 27 = 3^3. It divides by 3, then 9, and finally 3.
print(is_power(9, 2))   # Expected: False, because 9 is not divisible by 2, so it's not a power of 2.
print(is_power(81, 3))  # Expected: True, since 81 = 3^4. It divides by 3, then 27, 9, and finally 3.
print(is_power(32, 5))  # Expected: False, because 32 is not divisible by 5, so it's not a power of 5.
