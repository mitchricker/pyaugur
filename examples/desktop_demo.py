from pyaugur import build_deck, shuffle_deck, deal_cards
from pyaugur.spreads import SPREADS, interpret_named_spread
from pyaugur.meanings_full import MAJOR_MEANINGS, MINOR_MEANINGS

# Build and shuffle deck
deck = build_deck()
shuffle_deck(deck)

# Deal 3 cards
cards = deal_cards(deck, 3)

# Combine major and minor meanings
meanings = {}
meanings.update(MAJOR_MEANINGS)
meanings.update(MINOR_MEANINGS)

# Interpret the spread
result = interpret_named_spread("three_card", cards, meanings)

# Print results
for r in result:
    print(f"{r['position']}: {r['card']} – {r['meaning']}")