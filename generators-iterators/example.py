"""Generators & iterators basics."""

from collections.abc import Iterator


def countdown(n: int) -> Iterator[int]:
    while n > 0:
        yield n
        n -= 1


if __name__ == "__main__":
    it = iter([1, 2, 3])
    print(next(it), next(it))

    print(list(countdown(5)))
    squares = (x * x for x in range(5))
    print(list(squares))
