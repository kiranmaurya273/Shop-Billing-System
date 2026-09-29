"""MODULE 2 - turning a cart of items into a final bill.
build_bill does the actual math, checkout_flow talks to the user."""
from config import GST_RATE
from inventory import reduce_stock
from storage import load_items, save_items
from validators import ask_float, ask_int, ask_text


def build_bill(items, cart, discount_percent=0):
    """cart is a list of (name, quantity). Returns a bill dict."""
    lines = []
    subtotal = 0.0
    for name, qty in cart:
        price = items[name]["price"]
        line_total = round(price * qty, 2)
        subtotal += line_total
        lines.append({"item": name, "qty": qty, "price": price, "line_total": line_total})

    discount_amount = round(subtotal * discount_percent / 100, 2)
    taxable = subtotal - discount_amount
    gst_amount = round(taxable * GST_RATE, 2)
    grand_total = round(taxable + gst_amount, 2)

    return {
        "lines": lines, "subtotal": round(subtotal, 2),
        "discount_percent": discount_percent, "discount_amount": discount_amount,
        "gst_amount": gst_amount, "grand_total": grand_total,
    }


def print_bill(bill):
    print("\n" + "=" * 40)
    print(" BILL")
    print("=" * 40)
    for line in bill["lines"]:
        print(f"  {line['item']:<15} {line['qty']} x {line['price']:.2f} = {line['line_total']:.2f}")
    print("-" * 40)
    print(f"  Subtotal        : {bill['subtotal']:.2f}")
    if bill["discount_percent"] > 0:
        print(f"  Discount ({bill['discount_percent']}%)  : -{bill['discount_amount']:.2f}")
    print(f"  GST              : {bill['gst_amount']:.2f}")
    print(f"  GRAND TOTAL      : {bill['grand_total']:.2f}")
    print("=" * 40 + "\n")


def checkout_flow():
    print("\n--- New Bill ---")
    items = load_items()
    if not items:
        print("Catalog is empty, add items first.")
        return None

    cart = []
    while True:
        print("Available items:", ", ".join(items))
        name = ask_text("Item name (or type 'done' to finish): ")
        if name.lower() == "done":
            break
        if name not in items:
            print("That item isn't in the catalog.")
            continue
        qty = ask_int(f"Quantity (stock: {items[name]['stock']}): ", 1)
        if qty > items[name]["stock"]:
            print("Not enough stock for that quantity.")
            continue
        cart.append((name, qty))
        print(f"Added {qty} x {name} to cart.")

    if not cart:
        print("Cart is empty, bill cancelled.")
        return None

    discount = ask_float("Discount percent (0 if none): ", 0, 100)
    bill = build_bill(items, cart, discount)

    for name, qty in cart:
        reduce_stock(items, name, qty)
    save_items(items)

    print_bill(bill)
    return bill
