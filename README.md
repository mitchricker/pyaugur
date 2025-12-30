# PyAugur

PyAugur is a lightweight, stand-alone Tarot card utility module compatible with both
Python and MicroPython. It provides a complete 78-card tarot deck, built-in card
meanings, and a collection of common tarot spreads.

Originally developed for an ESP32 project using MicroPython, PyAugur is designed to be simple,
portable, and dependency-free: making it suitable for embedded systems, games,
and creative coding projects.

---

## Features

- Full 78-card Tarot deck (Major & Minor Arcana)
- Built-in card meanings
- Predefined tarot spreads (Celtic Cross, Three-Card, Year Ahead, etc.)
- Deck shuffling and card dealing utilities
- Works with standard Python and MicroPython
- No external dependencies

---

## Installation

PyAugur is a single-file module that can easily be used as a "drop-in" to your project.

Simply copy `pyaugur.py` into your project directory:

```text
your_project/
├── pyaugur.py
└── main.py
```

Then import it:

```python
import pyaugur
```

## Basic Usage
```python
from pyaugur import tarot_deck, shuffle_deck, deal_cards, interpret_named_spread

deck = tarot_deck.copy()
shuffle_deck(deck)

cards = deal_cards(deck, 3)
reading = interpret_named_spread("three_card", cards)

for entry in reading:
    print(entry["position"])
    print(entry["card"])
    print(entry["meaning"])
    print()
```
## Available Spreads

PyAugur includes several predefined spreads:

- one_card
- two_card
- three_card
- relationship
- celtic_cross
- horseshoe
- astrological
- career
- shadow
- year
- elemental
- chakra
- decision
- financial

Each spread defines its own positions and required card count.

## Design Notes

- Meanings are stored as plain strings for easy customization.
- All data structures use standard Python types for MicroPython compatibility.
- Procedural, stateless API to minimize memory usage.
