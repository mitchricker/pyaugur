try:
    import random
except ImportError:
    import urandom as random  # MicroPython fallback for ESP32

# Try to import full meanings, fallback to stub (ESP32)
try:
    from .meanings_full import ALL_MEANINGS
except ImportError:
    from .meanings_stub import ALL_MEANINGS

# Separate major & minor arcana from ALL_MEANINGS
MAJOR_ARCANA = [card for card in ALL_MEANINGS if " of " not in card]
MINOR_ARCANA = [card for card in ALL_MEANINGS if " of " in card]


def build_deck():
    """
    Create a new unshuffled tarot deck.

    Returns:
        list[str]: A list of 78 tarot cards (major and minor arcana).
    """
    return MAJOR_ARCANA + MINOR_ARCANA


def shuffle_deck(deck):
    """
    Shuffle a deck of cards in place.

    Args:
        deck (list[str]): The deck of cards to shuffle.

    Returns:
        None
    """
    random.shuffle(deck)


def deal_cards(deck, count):
    """
    Deal a specific number of cards from the deck.

    Args:
        deck (list[str]): The deck to draw cards from.
        count (int): Number of cards to deal.

    Raises:
        ValueError: If the deck does not have enough cards.

    Returns:
        list[str]: The cards drawn from the deck.
    """
    if count > len(deck):
        raise ValueError("Not enough cards in deck")
    return [deck.pop() for _ in range(count)]


def deal_cards_reversals(deck, count, reversal_chance=0.5):
    """
    Deal cards and optionally mark some as reversed.

    Args:
        deck (list[str]): The deck to draw cards from.
        count (int): Number of cards to deal.
        reversal_chance (float, optional): Probability each card is reversed (0.0–1.0). Defaults to 0.5.

    Returns:
        list[dict]: Each card represented as a dict with keys:
            - 'card' (str): The card name.
            - 'reversed' (bool): True if the card is reversed.
    """
    cards = deal_cards(deck, count)
    result = []
    for c in cards:
        reversed_flag = random.random() < reversal_chance
        result.append({"card": c, "reversed": reversed_flag})
    return result


def interpret_spread(cards, positions, meanings):
    """
    Interpret a tarot spread by mapping cards to positions and meanings.

    Args:
        cards (list[str]): The drawn cards.
        positions (list[str]): Names of the positions in the spread.
        meanings (dict): Mapping of card names to textual meanings.

    Raises:
        ValueError: If the number of cards does not match the number of positions.

    Returns:
        list[dict]: Each dict contains:
            - 'position' (str): The position name.
            - 'card' (str): The card name.
            - 'meaning' (str): The card's meaning.
    """
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
