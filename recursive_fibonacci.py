def fibonacci(n):
    """
    Returns the n-th term of the Fibonacci sequence using recursion.

    :param n: The position in the sequence (starting from 0).
    :return: The value of the n-th Fibonacci term.
    """
    # Base case
    if n <= 1:
        return n

    # Recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)


# Testing the function
if __name__ == "__main__":
    print(f"6th Fibonacci term: {fibonacci(6)}")
    print(f"13th Fibonacci term: {fibonacci(7)}")
    print(f"14th Fibonacci term: {fibonacci(8)}")
    print(f"15th Fibonacci term: {fibonacci(9)}")