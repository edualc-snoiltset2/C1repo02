def sum_even(numbers):
    """Return the sum of the even integers in ``numbers``.

    Raises:
        TypeError: if ``numbers`` is not a list or tuple, or if any element
            is not an integer. Booleans are rejected even though ``bool`` is
            a subclass of ``int``, and floats are rejected even when they
            hold a whole number (e.g. 4.0).
    """
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(
            f"numbers must be a list or tuple, got {type(numbers).__name__}"
        )
    for index, n in enumerate(numbers):
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError(
                f"element at index {index} must be an int, "
                f"got {type(n).__name__}: {n!r}"
            )
    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    print(sum_even([1, 2, 3, 4, 5, 6]))  # 12
