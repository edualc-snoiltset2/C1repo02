def sum_even(numbers):
    """Return the sum of the even numbers in ``numbers``.

    Non-integral values (e.g. 3.5) are never even and are skipped;
    integral floats such as 4.0 count as even.
    """
    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    print(sum_even([1, 2, 3, 4, 5, 6]))  # 12
