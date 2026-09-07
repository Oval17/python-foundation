"""Dataclasses basics."""

from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    age: int
    tags: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Point:
    x: float
    y: float


if __name__ == "__main__":
    u = User(name="ada", age=36, tags=["ml"])
    print(u)
    print(Point(x=1.0, y=2.0))
