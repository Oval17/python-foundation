"""Context managers basics."""

from contextlib import contextmanager


class Timer:
    def __enter__(self):
        import time

        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        import time

        print(f"elapsed: {time.perf_counter() - self._start:.6f}s")
        return False


@contextmanager
def managed_resource(name: str):
    print(f"acquire {name}")
    try:
        yield name
    finally:
        print(f"release {name}")


if __name__ == "__main__":
    with Timer():
        print("working...")

    with managed_resource("db") as r:
        print(f"using {r}")
