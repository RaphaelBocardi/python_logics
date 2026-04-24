def countdown(n):
    """
    Prints a countdown from n to 0 using recursion.
    """
    # Base case
    if n < 0:
        print("Blast off!")
        return

    # Recursive step
    print(n)
    countdown(n - 1)

# Calling the function
countdown(13)