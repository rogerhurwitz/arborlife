import math


def solve_cubic(a, b, c, d):
    p = -b / (3 * a)
    q = math.pow(p, 3) + (b * c - 3 * a * d) / (6 * math.pow(a, 2))
    r = c / (3 * a)

    x = (
        math.pow(
            q + (math.pow(math.pow(q, 2) + (math.pow(r - math.pow(p, 2), 3)), 0.5)), 1 / 3,
        )
        + math.pow(
            q - (math.pow(math.pow(q, 2) + (math.pow(r - math.pow(p, 2), 3)), 0.5)), 1 / 3,
        )
        + p
    )

    return x
