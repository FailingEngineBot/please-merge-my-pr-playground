def parse(text: str) -> dict[str, str]:
    """Parse KEY=VALUE lines."""
    pairs = (line.split('=', 1) for line in text.splitlines() if line)
    return {k.strip(): v.strip() for k, v in pairs}
