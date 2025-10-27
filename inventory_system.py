"""Simple inventory system (lab exercise).

This script provides minimal inventory operations used in the lab:
add_item, remove_item, get_qty, load_data, save_data, print_data,
and check_low_items. It is intentionally small and safe to run.
"""

import json
from datetime import datetime

# Global variable holding item -> quantity mapping
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add qty (int) of item (str) to stock_data; optionally append to logs."""
    if not isinstance(item, str) or not item.strip():
        raise ValueError("item must be a non-empty string")

    try:
        qty = int(qty)
    except (TypeError, ValueError) as exc:
        raise ValueError("qty must be an integer") from exc

    if logs is None:
        logs = []

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove qty of item from stock_data if present."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Item not found in stock_data; ignore silently
        return
    except TypeError as exc:
        # Wrong data type provided -> preserve context
        raise ValueError(
            "Invalid types passed to remove_item(item, qty)"
        ) from exc


def get_qty(item):
    """Return quantity for item; raise KeyError if not present."""
    if item not in stock_data:
        raise KeyError(f"{item} not in inventory")
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load stock data from JSON file into the global stock_data.

    If the file doesn't exist or contains invalid JSON, start with an
    empty dict.
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}
    except json.JSONDecodeError:
        stock_data = {}


def save_data(file="inventory.json"):
    """Save stock_data to JSON file using UTF-8 encoding."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
    except (TypeError, OSError) as exc:
        raise RuntimeError("Failed to save inventory data") from exc


def print_data():
    """Print a simple items report to stdout."""
    print("Items Report")
    for item in stock_data:
        print(item, "->", stock_data[item])


def check_low_items(threshold=5):
    """Return list of items whose quantity is below threshold."""
    result = []
    for item in stock_data:
        if stock_data[item] < threshold:
            result.append(item)
    return result


def main():
    """Small demo to exercise the inventory functions."""
    add_item("apple", 10)
    add_item("banana", -2)
    # Demonstrating validation: this would raise an error if uncommented
    # add_item(123, "ten")  # invalid types, no check

    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()
    print_data()
    print("eval used")


if __name__ == "__main__":
    main()
