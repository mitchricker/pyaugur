# PyAugur

PyAugur is a lightweight, stand-alone Tarot card utility library compatible with both
Python (CPython) and MicroPython. It provides a full 78-card tarot deck, built-in
card meanings, and a collection of common tarot spreads.

Originally developed for ESP32 projects using MicroPython, PyAugur is designed to be simple,
portable, and dependency-free—making it suitable for embedded systems, games,
and creative coding projects.

---

## Features

- Full 78-card Tarot deck (Major & Minor Arcana)
- Built-in card meanings:
  - `meanings_full.py` for desktop / Python (detailed interpretations)
  - `meanings_stub.py` for ESP32 / MicroPython (minimal keywords)
- Predefined tarot spreads (Celtic Cross, Three-Card, Year Ahead, etc.)
- Deck shuffling and card dealing utilities
- Optional reversed card support
- Works with standard Python and MicroPython
- No external dependencies

---

## Installation

PyAugur uses a `src/pyaugur` package layout and can be installed via **Poetry** or
used as a drop-in module.

**Poetry installation:**

```bash
poetry add git+https://github.com/mitchricker/pyaugur.git
```

**Manual usage:**

Copy the pyaugur folder into your project:

```
your_project/
├── pyaugur/
│   ├── __init__.py
│   ├── core.py
│   ├── spreads.py
│   ├── meanings_full.py
│   └── meanings_stub.py
└── main.py
```

Then import it in your code:

```Python
from pyaugur import build_deck, shuffle_deck, deal_cards, interpret_spread
```

---

## Available Spreads

PyAugur includes several predefined spreads:

- `one_card`
- `two_card`
- `three_card`
- `relationship`
- `celtic_cross`
- `horseshoe`
- `astrological`
- `career`
- `shadow`
- `year`
- `elemental`
- `chakra`
- `decision`
- `financial`

Each spread defines its own positions and required card count.

---

## Design Notes

  - Meanings are plain strings for easy customization.
  - All data structures use standard Python types for MicroPython compatibility.
  - Procedural, stateless API minimizes memory usage.
  - Provides both full and minimal meanings for desktop vs. embedded targets.
