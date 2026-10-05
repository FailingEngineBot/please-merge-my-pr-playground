def total_cents(items: list[tuple[int, int]]) -> int:
    """Sum of price_cents * quantity."""
    return sum(price * qty for price, qty in items)
