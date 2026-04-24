def factorial(n):
    """
    Calculates the factorial of a number using recursion.

    :param n: The integer number to calculate.
    :return: The factorial result or an error message for negative inputs.
    """
    # Input validation
    if n < 0:
        return "Error: Negative numbers are not allowed"

    # Base case
    if n <= 1:
        return 1

    # Recursive step
    return n * factorial(n - 1)


# Testing the function
if __name__ == "__main__":
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Factorial of 6: {factorial(6)}")
    print(f"Factorial of 7: {factorial(7)}")
    print(f"Factorial of 8: {factorial(8)}")
    print(f"Factorial of 9: {factorial(9)}")
    print(f"Factorial of 10: {factorial(10)}")