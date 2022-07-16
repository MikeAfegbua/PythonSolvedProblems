"""
high level support for doing this and that.
"""
counter = 0
for num in range(1, 15):
    if num % 2 == 0:
        counter += 1
        print(num)
print(f"we have {counter} even numbers")
