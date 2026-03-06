"""
Minimal Tarot card meanings for ESP32 / MicroPython.

Includes:
- Full Major Arcana with short descriptive phrases.
- Condensed Minor Arcana keywords per suit.
"""

MAJOR_MEANINGS = {
    "The Fool": "new beginnings, adventure",
    "The Magician": "action, skill, power",
    "The High Priestess": "intuition, mystery",
    "The Empress": "nurturing, abundance",
    "The Emperor": "authority, stability",
    "The Hierophant": "tradition, guidance",
    "The Lovers": "love, choices",
    "The Chariot": "willpower, victory",
    "Strength": "courage, patience",
    "The Hermit": "reflection, solitude",
    "Wheel of Fortune": "change, cycles",
    "Justice": "fairness, truth",
    "The Hanged Man": "perspective, letting go",
    "Death": "transformation, endings",
    "Temperance": "balance, moderation",
    "The Devil": "temptation, attachment",
    "The Tower": "sudden change, upheaval",
    "The Star": "hope, inspiration",
    "The Moon": "illusion, intuition",
    "The Sun": "joy, clarity",
    "Judgement": "rebirth, reflection",
    "The World": "completion, fulfillment",
}

# Minor Arcana meanings per suit
SUIT_KEYWORDS = {
    "Wands": [
        "inspiration, beginnings",
        "planning, progress",
        "growth, foresight",
        "stability, celebration",
        "challenge, conflict",
        "success, victory",
        "perseverance, defense",
        "action, movement",
        "resilience, courage",
        "completion, responsibility",
        "curiosity, learning",
        "adventure, ambition",
        "leadership, vision",
        "authority, mastery",
    ],
    "Cups": [
        "emotional beginnings",
        "partnership, union",
        "joy, friendship",
        "contemplation, reevaluation",
        "loss, regret",
        "nostalgia, memories",
        "choices, illusions",
        "transition, release",
        "contentment, satisfaction",
        "family, emotional fulfillment",
        "imagination, growth",
        "romance, charm",
        "compassion, empathy",
        "emotional control, leadership",
    ],
    "Swords": [
        "clarity, new ideas",
        "indecision, choices",
        "heartbreak, sorrow",
        "rest, recovery",
        "conflict, loss",
        "transition, relief",
        "deception, betrayal",
        "restriction, limitation",
        "anxiety, worry",
        "endings, crisis",
        "curiosity, vigilance",
        "action, decisiveness",
        "intellect, independence",
        "strategy, authority",
    ],
    "Pentacles": [
        "opportunity, manifestation",
        "balance, adaptability",
        "collaboration, skill",
        "stability, security",
        "financial challenge, loss",
        "generosity, giving",
        "evaluation, patience",
        "diligence, skill",
        "abundance, self-sufficiency",
        "wealth, legacy",
        "studiousness, ambition",
        "practicality, dedication",
        "nurturing, resourcefulness",
        "success, control",
    ],
}

# Build Minor Arcana dictionary dynamically
MINOR_MEANINGS = {}
for suit, meanings in SUIT_KEYWORDS.items():
    for i, rank in enumerate(
        [
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
    ):
        card_name = f"{rank} of {suit}"
        MINOR_MEANINGS[card_name] = meanings[i]

# Combine all into one dictionary
ALL_MEANINGS = {}
ALL_MEANINGS.update(MAJOR_MEANINGS)
ALL_MEANINGS.update(MINOR_MEANINGS)
