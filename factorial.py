# ==============================================================================
# * Factorial using Recursion
# ! Time complexity - O(n!)
# ==============================================================================
def factorial(n: int) -> int:
    return 1 if n == 1 else n * factorial(n - 1)


print(factorial(100))
