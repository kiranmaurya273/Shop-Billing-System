"""Settings used by every other file. Change values here, not in the code."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ITEMS_FILE = os.path.join(BASE_DIR, "data", "items.json")
SALES_FILE = os.path.join(BASE_DIR, "data", "sales.json")
REPORTS_DIR = os.path.join(BASE_DIR, "data", "reports")

GST_RATE = 0.18       # 18% GST, change if your state/product differs
LOW_STOCK_LEVEL = 5   # print a warning once stock drops to this or below
