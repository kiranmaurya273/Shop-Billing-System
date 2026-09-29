"""MODULE 3 - saving completed bills to a sales log and reporting on them."""
import os
from datetime import date, datetime

from config import REPORTS_DIR
from storage import load_sales, save_sales


def record_sale(bill):
    sales = load_sales()
    sale = {**bill, "date": date.today().isoformat()}
    sales.append(sale)
    save_sales(sales)


def sales_summary():
    sales = load_sales()
    if not sales:
        return "No sales recorded yet."

    total_revenue = sum(s["grand_total"] for s in sales)
    item_counts = {}
    for s in sales:
        for line in s["lines"]:
            item_counts[line["item"]] = item_counts.get(line["item"], 0) + line["qty"]
    best_seller = max(item_counts, key=item_counts.get)

    lines = ["SALES SUMMARY", "=" * 40,
              f"Total bills      : {len(sales)}",
              f"Total revenue    : {total_revenue:.2f}",
              f"Best-selling item: {best_seller} ({item_counts[best_seller]} sold)"]
    return "\n".join(lines)


def view_sales_history():
    sales = load_sales()
    if not sales:
        print("\nNo sales recorded yet.")
        return
    print(f"\n{'Date':<12}{'Items':<8}{'Total':<10}")
    print("-" * 30)
    for s in sales:
        print(f"{s['date']:<12}{len(s['lines']):<8}{s['grand_total']:<10.2f}")


def export_report():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(REPORTS_DIR, f"sales_report_{timestamp}.txt")
    with open(filename, "w") as f:
        f.write(sales_summary())
    print(f"Report saved to {filename}")
