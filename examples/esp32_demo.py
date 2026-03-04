"""
ESP32 MicroPython demo for pyaugur.
Uses minimal stub meanings to reduce memory usage.
"""

from pyaugur import build_deck, shuffle_deck, deal_cards
from pyaugur.spreads import SPREADS, interpret_named_spread
from pyaugur.meanings_stub import MAJOR_MEANINGS, MINOR_MEANINGS

# build and shuffle deck
deck = build_deck()
shuffle_deck(deck)

# deal 3 cards
cards = deal_cards(deck, 3)

# combine stub meanings
meanings = {}
meanings.update(MAJOR_MEANINGS)
meanings.update(MINOR_MEANINGS)

# interpret spread
result = interpret_named_spread("three_card", cards, meanings)

# print results
for r in result:
    print("{}: {} – {}".format(r["position"], r["card"], r["meaning"]))