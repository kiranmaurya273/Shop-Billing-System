"""MODULE 1 - the item catalog (add/view/remove, stock levels).
Items are stored as {name: {"price": p, "stock": qty}}."""
from config import LOW_STOCK_LEVEL
from storage import load_items, save_items
from validators import ask_float, ask_int, ask_text


def add_item(items, name, price, stock):
    items[name] = {"price": price, "stock": stock}


def remove_item(items, name):
    if name in items:
        del items[name]
        return True
    return False


def reduce_stock(items, name, quantity):
    """Returns True if there was enough stock and it was reduced."""
    if name not in items or items[name]["stock"] < quantity:
        return False
    items[name]["stock"] -= quantity
    return True


def add_item_flow():
    print("\n--- Add Item to Catalog ---")
    items = load_items()
    name = ask_text("Item name: ")
    price = ask_float("Price per unit (Rs): ", 0.01)
    stock = ask_int("Stock quantity: ", 0)
    add_item(items, name, price, stock)
    save_items(items)
    print(f"Added/updated '{name}': Rs{price} x {stock} in stock.")


def view_items_flow():
    items = load_items()
    if not items:
        print("\nNo items in catalog yet.")
        return
    print(f"\n{'Item':<20}{'Price':<10}{'Stock':<8}")
    print("-" * 38)
    for name, info in items.items():
        flag = "  <- LOW STOCK" if info["stock"] <= LOW_STOCK_LEVEL else ""
        print(f"{name:<20}{info['price']:<10.2f}{info['stock']:<8}{flag}")


def remove_item_flow():
    view_items_flow()
    items = load_items()
    if not items:
        return
    name = ask_text("Item name to remove: ")
    if remove_item(items, name):
        save_items(items)
        print(f"Removed '{name}'.")
    else:
        print(f"No item called '{name}'.")
