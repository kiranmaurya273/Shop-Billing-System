# Shop Billing System

A command-line billing system for a small shop - you keep a catalog of
items with price and stock, generate bills with discount and GST applied,
and it keeps a sales log so you can see how the shop is doing. Built for
my first-semester Python course project.

## Why I made this

Wanted to do something a bit more "business-y" than just a personal
tracker - my uncle runs a small stationery shop and does all his billing
on paper, so I based this loosely on what he'd actually need: add stock,
bill a customer, apply a discount sometimes, and GST always gets added.
Also wanted to practice something with stock management since that adds
a bit more logic than a plain CRUD app.

## What it does

- Add items to the catalog (name, price, stock quantity) - adding the
  same name again just updates price/stock instead of duplicating
- View the catalog, with a low-stock warning if something's running out
- Remove an item from the catalog
- New bill: pick items and quantities from the catalog, checks stock
  before letting you add too much, then apply an optional discount %.
  GST (18% by default) gets added after the discount, not before - that
  tripped me up initially, discount has to come off the subtotal first
- Stock automatically goes down after a bill is made
- Sales history - see every past bill (date, number of items, total)
- Sales summary - total revenue, total bills, and the best-selling item
- Export the summary as a text file
- Everything (catalog + sales) is saved between runs

## Project layout

```
shop_billing/
├── main.py          # run this - the menu loop
├── config.py        # file paths, GST rate, low stock threshold
├── validators.py     # input checking
├── inventory.py       # item catalog: add/view/remove, stock changes
├── billing.py          # the actual bill math + checkout flow
├── sales.py             # saving completed bills, sales history & summary
├── tests/
│   └── test_shop_billing.py
└── data/
    ├── items.json          # catalog, created automatically
    ├── sales.json           # sales log, created automatically
    └── reports/
```

Kept `inventory.py` (the catalog) and `billing.py` (the actual bill/math)
separate on purpose - billing needs to read stock but shouldn't be the
thing managing it, felt cleaner to have one file own the catalog and
another just consume it.

## How to run it

Just Python 3, nothing to install.

```
cd shop_billing
python3 main.py
```

Add a couple of items to the catalog first (option 1), then try making a
bill (option 4).

## Running the tests

```
python3 -m unittest discover tests
```

Covers stock reduction when there's enough/not enough stock, removing an
item that does/doesn't exist, and the bill math itself - specifically
that discount is applied before GST, since that's the part most likely to
go wrong.

## Some things worth knowing

- GST rate is 18% by default (`GST_RATE` in config.py), change it if your
  scenario needs a different rate
- Low stock warning shows once an item's stock drops to 5 or below
  (`LOW_STOCK_LEVEL` in config.py)
- If items.json or sales.json gets deleted or corrupted, the program
  starts fresh with empty data instead of crashing

## Possible improvements later

- Multiple discount types (flat amount vs percentage)
- Return/refund handling
- A proper invoice number instead of just a timestamp filename
