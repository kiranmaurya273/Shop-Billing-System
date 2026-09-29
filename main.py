"""Shop Billing System - run this file:  python main.py"""
from billing import checkout_flow
from inventory import add_item_flow, remove_item_flow, view_items_flow
from sales import export_report, record_sale, sales_summary, view_sales_history
from validators import ask_choice


def new_bill_flow():
    bill = checkout_flow()
    if bill:
        record_sale(bill)


def main():
    print("=" * 40 + "\n SHOP BILLING SYSTEM\n" + "=" * 40)
    menu = {
        "1": ("Add item to catalog", add_item_flow),
        "2": ("View catalog", view_items_flow),
        "3": ("Remove item", remove_item_flow),
        "4": ("New bill (checkout)", new_bill_flow),
        "5": ("View sales history", view_sales_history),
        "6": ("Sales summary", lambda: print("\n" + sales_summary())),
        "7": ("Export sales report", export_report),
    }
    while True:
        print("\n" + "\n".join(f"  {k}. {v[0]}" for k, v in menu.items()) + "\n  8. Exit")
        choice = ask_choice("Enter choice (1-8): ", list(menu) + ["8"])
        if choice == "8":
            print("Goodbye!")
            break
        menu[choice][1]()


if __name__ == "__main__":
    main()
