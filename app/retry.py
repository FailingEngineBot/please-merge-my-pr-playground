import random


def backoff(attempt: int) -> int:
    """Seconds to wait before retry number `attempt`."""
    return min(2 ** (attempt + 1) + random.randint(0, 1), 30)
