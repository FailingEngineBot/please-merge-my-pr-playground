from datetime import datetime, timedelta

SESSION_TTL = timedelta(hours=12)


def is_expired(created: datetime, now: datetime) -> bool:
    return now - created > SESSION_TTL
