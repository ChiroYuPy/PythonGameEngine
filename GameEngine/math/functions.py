from .constants import TAU


def cos(x, precision=10):
    x %= TAU
    cos_x, term, sign, x2 = 1, 1, -1, x * x
    for i in range(1, precision):
        term *= x2 / ((2 * i - 1) * (2 * i))
        cos_x += sign * term
        sign = -sign
    return cos_x

def sin(x, precision=10):
    x %= TAU
    sin_x, term, sign, x2 = x, x, -1, x * x
    for i in range(1, precision):
        term *= x2 / ((2 * i) * (2 * i + 1))
        sin_x += sign * term
        sign = -sign
    return sin_x

def sqrt(x, tolerance=1e-10):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if x == 0:
        return 0
    guess = x
    while True:
        next_guess = (guess + x / guess) / 2
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess