import unittest

from billing.invoice import total_cents


class InvoiceTest(unittest.TestCase):
    def test_total(self) -> None:
        self.assertEqual(total_cents([(250, 2), (100, 1)]), 600)
