from .patterns import PATTERNS


def get(datestring):
    """
    >>> get("2022-05-11")
    '%Y-%m-%d'
    >>> get("5/11/22")
    '%-m/%-d/%-y'
    >>> get("May 11, 2022")
    '%b %-d, %Y'
    """
    for s, p in PATTERNS.items():
        if p.match(datestring):
            return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
