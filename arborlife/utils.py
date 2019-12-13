import math
import numpy as np
import scipy.stats as stats


def calc_cubic(a, b, c, d):
    p = -b / (3 * a)
    q = math.pow(p, 3) + (b * c - 3 * a * d) / (6 * math.pow(a, 2))
    r = c / (3 * a)

    x = (
        math.pow(
            q + (math.pow(math.pow(q, 2) + (math.pow(r - math.pow(p, 2), 3)), 0.5)), 1 / 3,     # noqa: E501
        )
        + math.pow(
            q - (math.pow(math.pow(q, 2) + (math.pow(r - math.pow(p, 2), 3)), 0.5)), 1 / 3,     # noqa: E501
        )
        + p
    )
    return x


def calc_truncnorm(mean, sd, *, clip_a=-np.inf, clip_b=np.inf):
    """Returns a float in a normal distribution (mean, sd) clipped (clip_a, clip_b)."""

    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.truncnorm.html
    return stats.truncnorm.rvs(
        a=(clip_a - mean) / sd, b=(clip_b - mean) / sd, loc=mean, scale=sd
    )
