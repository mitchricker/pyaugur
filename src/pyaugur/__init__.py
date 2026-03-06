from .core import (
    build_deck,
    shuffle_deck,
    deal_cards,
    deal_cards_reversals,
    interpret_spread,
)

from .spreads import interpret_named_spread, SPREADS

# Attempt full meanings first; fallback to stub for ESP32 / MicroPython
try:
    from .meanings_full import ALL_MEANINGS
except ImportError:
    from .meanings_stub import ALL_MEANINGS

__all__ = [
    # Core
    "build_deck",
    "shuffle_deck",
    "deal_cards",
    "deal_cards_reversals",
    "interpret_spread",
    # Spreads
    "interpret_named_spread",
    "SPREADS",
    # Meanings
    "ALL_MEANINGS",
]
