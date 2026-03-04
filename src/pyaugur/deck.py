# List of all 22 Major Arcana tarot cards
MAJOR_ARCANA = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",
]

# Suits in the Minor Arcana
SUITS = ["Wands", "Cups", "Swords", "Pentacles"]

# Ranks in each suit of the Minor Arcana
RANKS = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Page",
    "Knight",
    "Queen",
    "King",
]


def build_deck():
    """
    Build a full 78-card tarot deck.

    Combines the Major Arcana cards with all combinations of
    Minor Arcana suits and ranks to produce a complete deck.

    Returns:
        list[str]: A list of card names in order: Major Arcana first,
                   followed by Minor Arcana.
    """
    deck = MAJOR_ARCANA[:]
    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{rank} of {suit}")
    return deck
