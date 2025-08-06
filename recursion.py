"""
recursion.py
Examples of recursion in Python
"""

def factorial(n):
    """Calculate factorial of n recursively"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Return nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Fibonacci(6):", fibonacci(6))
