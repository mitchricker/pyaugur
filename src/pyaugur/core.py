try:
    import random
except ImportError:
    import urandom as random  # MicroPython fallback

# Try to import full meanings, fallback to stub (ESP32)
try:
    from .meanings_full import ALL_MEANINGS
except ImportError:
    from .meanings_stub import ALL_MEANINGS

# Separate major & minor arcana from ALL_MEANINGS
MAJOR_ARCANA = [card for card in ALL_MEANINGS if " of " not in card]
MINOR_ARCANA = [card for card in ALL_MEANINGS if " of " in card]


def build_deck():
    """Return a new unshuffled tarot deck with 78 cards."""
    return MAJOR_ARCANA + MINOR_ARCANA


def shuffle_deck(deck):
    """Shuffle the deck in place."""
    random.shuffle(deck)


def deal_cards(deck, count):
    """Deal `count` cards from the deck."""
    if count > len(deck):
        raise ValueError("Not enough cards in deck")
    return [deck.pop() for _ in range(count)]


def deal_cards_reversals(deck, count, reversal_chance=0.5):
    """Deal cards with optional reversed flags."""
    cards = deal_cards(deck, count)
    result = []
    for c in cards:
        reversed_flag = random.random() < reversal_chance
        result.append({"card": c, "reversed": reversed_flag})
    return result


def interpret_spread(cards, positions, meanings):
    """Interpret a spread using positions and meanings."""
    if len(cards) != len(positions):
        raise ValueError("Card count mismatch")

    output = []
    for pos, card in zip(positions, cards):
        meaning = meanings.get(card, "No meaning available.")
        output.append(
            {
                "position": pos,
                "card": card,
                "meaning": meaning,
            }
        )
    return output
