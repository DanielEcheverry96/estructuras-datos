def find_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return find_fibonacci(n - 1) + find_fibonacci(n - 2)


print(find_fibonacci(6))
