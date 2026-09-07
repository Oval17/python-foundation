"""Async / await basics."""

import asyncio


async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} done in {delay}s"


async def main() -> None:
    results = await asyncio.gather(
        fetch("a", 0.1),
        fetch("b", 0.05),
    )
    for r in results:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
