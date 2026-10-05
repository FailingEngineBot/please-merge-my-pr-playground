def parse(text: str) -> dict[str, str]:
    """Parse KEY=VALUE lines."""
    out: dict[str, str] = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line:
            continue
        if '=' not in line:
            raise ValueError(f'line {n}: expected KEY=VALUE')
        k, v = line.split('=', 1)
        out[k.strip()] = v.strip()
    return out
