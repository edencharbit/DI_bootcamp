# #  Exercise 4: Floats
#
# Recap: Float vs. Integer
# Integer (int): A whole number without a fractional part (e.g., 2, -5, 42).
# Float (floating-point number): A number that contains a decimal point (
# 1.5, 3.0, 4.99).
#
# The main difference is that floats are used when precision is needed (
# decimals), whereas integers are used for counting or discrete values. In
# Python, even if a number is mathematically an integer (like 3), writing it
# as 3.0 makes it a float.

mixed_lst = []
for i in range(3, 11):
    val = i / 2
    if val.is_integer():
        mixed_lst.append(int(val))
    else:
        mixed_lst.append(val)
print(mixed_lst)