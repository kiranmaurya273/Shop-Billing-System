import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from billing import build_bill
from inventory import add_item, reduce_stock, remove_item


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.items = {}
        add_item(self.items, "Pen", 10.0, 50)

    def test_add_item(self):
        self.assertEqual(self.items["Pen"], {"price": 10.0, "stock": 50})

    def test_reduce_stock_enough(self):
        self.assertTrue(reduce_stock(self.items, "Pen", 5))
        self.assertEqual(self.items["Pen"]["stock"], 45)

    def test_reduce_stock_not_enough(self):
        self.assertFalse(reduce_stock(self.items, "Pen", 100))
        self.assertEqual(self.items["Pen"]["stock"], 50)  # unchanged

    def test_remove_item(self):
        self.assertTrue(remove_item(self.items, "Pen"))
        self.assertFalse(remove_item(self.items, "Pen"))  # already gone


class BillingTests(unittest.TestCase):
    def setUp(self):
        self.items = {"Notebook": {"price": 50.0, "stock": 20},
                      "Pen": {"price": 10.0, "stock": 50}}

    def test_subtotal_and_total_no_discount(self):
        bill = build_bill(self.items, [("Notebook", 2), ("Pen", 3)], discount_percent=0)
        self.assertEqual(bill["subtotal"], 130.0)   # 100 + 30
        self.assertEqual(bill["gst_amount"], round(130.0 * 0.18, 2))
        self.assertEqual(bill["grand_total"], round(130.0 * 1.18, 2))

    def test_discount_applied_before_gst(self):
        bill = build_bill(self.items, [("Notebook", 2)], discount_percent=10)
        self.assertEqual(bill["discount_amount"], 10.0)   # 10% of 100
        taxable = 90.0
        self.assertEqual(bill["gst_amount"], round(taxable * 0.18, 2))


if __name__ == "__main__":
    unittest.main()
