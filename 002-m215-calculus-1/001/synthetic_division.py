def synthetic_division(zero_candidate, coefficients):
    """ Performs synthetic division to determine whether the
    provided zero is a factor of a polynomial with the
    coefficients provided.

    Args:
        zero_candidate: possible root of polynomial, e.g. z in the expression (x-z) = 0
        coefficients: list of coefficients in polynomial
    Returns: boolean
    """
    i = 1
    # initialize to leading coefficient
    remainder = coefficients[0]
    # iterate starting from second coefficient
    for coefficient in coefficients[1:]:
        intermediate = zero_candidate * remainder
        remainder = coefficient + intermediate
        i += 1
        if i == len(coefficients):
            # we're going to approximate since floating point
            # numbers don't handle division well
            is_factor = remainder > 0 - .000000001 and \
                remainder < 0 + .000000001
            return is_factor

# Example usage
synthetic_division(1/3, [3, -8, -8, 8]) # Output: False
synthetic_division(2/3, [3, -8, -8, 8]) # Output: True
synthetic_division(3/2, [2, -3, -11, 6]) # Output: False
synthetic_division(1/2, [2, -3, -11, 6]) # Output: True
