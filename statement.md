# Problem Statement

## Problem

Small shops often still do billing by hand - adding up item prices,
working out a discount, then adding GST on top, all on paper or in a
notebook. It's slow and easy to make an arithmetic mistake, and there's no
easy way to see stock levels or which items are actually selling well.

## Scope

- Manage an item catalog (add/view/remove, with price and stock)
- Generate a bill from a cart of items, with an optional discount applied
  before GST
- Automatically reduce stock after a sale, and warn when stock is low
- Keep a sales log and show summary stats (revenue, best-selling item)
- Save all data between runs, export a sales summary to a file

Not doing: multiple discount types, refunds/returns, or a GUI - keeping
this to a command-line tool for now.

## Target users

Small shop owners (or students building a class project around one) who
want a lightweight way to generate bills and track stock without a full
POS system.

## High-level features

1. Item catalog management (add/view/remove, stock tracking)
2. Billing (cart, discount, GST calculation, printed bill)
3. Sales log and reporting (history, summary stats, save/load persistence)
