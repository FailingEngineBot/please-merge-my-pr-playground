import unittest

from app.retry import backoff


class BackoffTest(unittest.TestCase):
    def test_first_retry_waits_one_second(self) -> None:
        self.assertEqual(backoff(0), 1)

    def test_capped_at_thirty(self) -> None:
        self.assertEqual(backoff(10), 30)
