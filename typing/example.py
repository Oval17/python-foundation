"""Typing basics: annotations + generics."""

from typing import Optional


def greet(name: str) -> str:
    return f"hello, {name}"


def first(xs: list[int]) -> Optional[int]:
    return xs[0] if xs else None


def counts(words: list[str]) -> dict[str, int]:
    out: dict[str, int] = {}
    for w in words:
        out[w] = out.get(w, 0) + 1
    return out


if __name__ == "__main__":
    print(greet("ada"))
    print(first([1, 2, 3]))
    print(first([]))
    print(counts(["a", "b", "a"]))
