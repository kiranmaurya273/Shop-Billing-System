"""Reading and writing items.json / sales.json. A missing or broken file
never crashes the program, it just starts with empty data."""
import json
import os

from config import ITEMS_FILE, SALES_FILE


def _load(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path) as f:
            content = f.read().strip()
            return json.loads(content) if content else default
    except (json.JSONDecodeError, OSError) as e:
        print(f"[Warning] Could not read {os.path.basename(path)} ({e}). Starting fresh.")
        return default


def _save(path, data):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return True
    except OSError as e:
        print(f"[Error] Could not save {os.path.basename(path)}: {e}")
        return False


def load_items():
    return _load(ITEMS_FILE, {})


def save_items(items):
    return _save(ITEMS_FILE, items)


def load_sales():
    return _load(SALES_FILE, [])


def save_sales(sales):
    return _save(SALES_FILE, sales)
