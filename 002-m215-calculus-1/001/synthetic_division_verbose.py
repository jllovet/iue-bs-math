def synthetic_division(zero_candidate, coefficients, verbose=False):
    """ Performs synthetic division to determine whether the provided zero is a
    factor of a polynomial with the coefficients provided.

    Args:
        zero_candidate: possible root of polynomial, e.g. z in the expression (x-z) = 0
        coefficients: list of coefficients in polynomial
    Returns: boolean
    """
    if verbose:
        print(
            "Performing synthetic division to check whether",
            zero_candidate, "\n"
            "is a factor of a polynomial with coefficients",
            coefficients,
            "\n"
        )
    i = 1
    remainder = coefficients[0] # initialize to leading coefficient
    if verbose:
        print("Initial remainder is set to leading coefficient:", remainder)
    for coefficient in coefficients[1:]: # iterate starting from second coefficient
        if verbose: 
            print("zero candidate:", zero_candidate)
            print("coefficient:", coefficient)
            print("previous remainder:", remainder)
        intermediate = zero_candidate * remainder
        if verbose:
            print("intermediate = zero_candidate * previous remainder:", intermediate)
        remainder = coefficient + intermediate
        if verbose:
            print("new remainder = coefficient + intermediate:", remainder, "\n")
        i += 1
        if i == len(coefficients):
            if verbose:
                print("Final result:", remainder, "\n")
            # we're going to approximate since floating point numbers don't handle division well
            is_factor = remainder > 0 - .000000001 and remainder < 0 + .000000001
            if verbose:
                print("Is Factor of Polynomial:", is_factor, "\n")
            return is_factor

# Example usage
# Printing non-verbose output
print(synthetic_division(1/3, [3, -8, -8, 8], verbose=False)) # Output: False
print(synthetic_division(2/3, [3, -8, -8, 8], verbose=False)) # Output: True
print(synthetic_division(3/2, [2, -3, -11, 6], verbose=False)) # Output: False

# Using function's verbose flag to print verbosely
synthetic_division(1/2, [2, -3, -11, 6], verbose=True) # Output: True
