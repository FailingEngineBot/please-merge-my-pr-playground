def total_cents(items: list[tuple[int, int]]) -> int:
    """Sum of price_cents * quantity."""
    return sum(price * qty for price, qty in items)


def with_tax(cents: int, rate_bp: int) -> int:
    """Add tax in basis points, rounding half up."""
    return cents + (cents * rate_bp + 5000) // 10000
