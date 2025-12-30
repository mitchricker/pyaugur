"""
pyaugur.py
A stand-alone module for Tarot deck operations.
Compatible with Python and MicroPython.
"""
from random import shuffle

major_arcana = {
    "The Fool": "New beginnings, adventure, and spontaneity.",
    "The Magician": "Manifestation, resourcefulness, and power.",
    "The High Priestess": "Intuition, unconscious knowledge, and mystery.",
    "The Empress": "Nurturing, abundance, and fertility.",
    "The Emperor": "Authority, structure, and stability.",
    "The Hierophant": "Tradition, conformity, and spiritual guidance.",
    "The Lovers": "Relationships, love, and choices.",
    "The Chariot": "Determination, control, and victory.",
    "Strength": "Courage, patience, and inner strength.",
    "The Hermit": "Introspection, solitude, and wisdom.",
    "Wheel of Fortune": "Change, cycles, and destiny.",
    "Justice": "Fairness, truth, and balance.",
    "The Hanged Man": "Letting go, suspension, and new perspectives.",
    "Death": "Transformation, endings, and new beginnings.",
    "Temperance": "Balance, moderation, and harmony.",
    "The Devil": "Temptation, materialism, and bondage.",
    "The Tower": "Sudden upheaval, chaos, and revelation.",
    "The Star": "Hope, inspiration, and renewal.",
    "The Moon": "Illusion, intuition, and the subconscious.",
    "The Sun": "Joy, success, and vitality.",
    "Judgement": "Reflection, reckoning, and rebirth.",
    "The World": "Completion, achievement, and fulfillment."
}

minor_arcana = {
    "Wands": {
        "Ace": "New beginnings, potential, and inspiration.",
        "2": "Planning, decisions, and progress.",
        "3": "Expansion, foresight, and leadership.",
        "4": "Stability, celebration, and harmony.",
        "5": "Conflict, competition, and challenge.",
        "6": "Victory, success, and recognition.",
        "7": "Perseverance, defense, and determination.",
        "8": "Movement, action, and swift progress.",
        "9": "Resilience, courage, and perseverance.",
        "10": "Burden, responsibility, and completion.",
        "Page": "Enthusiasm, exploration, and creativity.",
        "Knight": "Action, adventure, and ambition.",
        "Queen": "Leadership, vision, and passion.",
        "King": "Authority, control, and mastery."
    },
    "Cups": {
        "Ace": "Emotional fulfillment, new relationships, and love.",
        "2": "Partnership, union, and harmony.",
        "3": "Joy, celebration, and friendship.",
        "4": "Discontent, contemplation, and reevaluation.",
        "5": "Loss, regret, and mourning.",
        "6": "Nostalgia, memories, and reconnection.",
        "7": "Choices, illusions, and fantasy.",
        "8": "Leaving behind, moving on, and transition.",
        "9": "Contentment, satisfaction, and wishes fulfilled.",
        "10": "Emotional fulfillment, family, and happiness.",
        "Page": "Imagination, intuition, and emotional growth.",
        "Knight": "Romance, charm, and idealism.",
        "Queen": "Compassion, empathy, and emotional depth.",
        "King": "Emotional control, authority, and leadership."
    },
    "Swords": {
        "Ace": "Clarity, truth, and new ideas.",
        "2": "Indecision, choices, and balance.",
        "3": "Heartbreak, sorrow, and separation.",
        "4": "Rest, recovery, and contemplation.",
        "5": "Conflict, loss, and strategy.",
        "6": "Transition, moving on, and relief.",
        "7": "Deception, strategy, and betrayal.",
        "8": "Restriction, limitation, and mental anguish.",
        "9": "Anxiety, worry, and sleeplessness.",
        "10": "Endings, betrayal, and crisis.",
        "Page": "Curiosity, intellect, and vigilance.",
        "Knight": "Action, conflict, and decisiveness.",
        "Queen": "Intellect, independence, and perception.",
        "King": "Authority, intellect, and strategic thinking."
    },
    "Pentacles": {
        "Ace": "Opportunity, prosperity, and manifestation.",
        "2": "Balance, adaptability, and multitasking.",
        "3": "Collaboration, skill, and mastery.",
        "4": "Stability, security, and possessiveness.",
        "5": "Financial loss, insecurity, and struggle.",
        "6": "Generosity, giving, and receiving.",
        "7": "Patience, evaluation, and growth.",
        "8": "Diligence, hard work, and skill development.",
        "9": "Abundance, self-sufficiency, and luxury.",
        "10": "Wealth, family, and legacy.",
        "Page": "Studiousness, ambition, and potential.",
        "Knight": "Practicality, dedication, and responsibility.",
        "Queen": "Nurturing, practicality, and resourcefulness.",
        "King": "Success, control, and financial acumen."
    }
}

tarot_deck = list(major_arcana.keys()) + [
    f"{rank} of {suit}" for suit in minor_arcana for rank in minor_arcana[suit]
]

SPREADS = {
    "one_card": ("One-Card Daily Draw", ["Daily Guidance"]),
    "two_card": ("Two-Card Choice", ["Option A", "Option B"]),
    "three_card": ("Three-Card Spread", ["Past", "Present", "Future"]),
    "relationship": (
        "Relationship Spread",
        ["Your Feelings", "Their Feelings", "Current State", "Strengths", "Challenges", "Potential Outcome"]
    ),
    "celtic_cross": (
        "Celtic Cross Spread",
        ["The Present", "The Challenge", "The Past", "The Future", "The Above", "The Below",
         "The Self", "The Environment", "The Hopes and Fears", "The Outcome"]
    ),
    "horseshoe": (
        "Horseshoe Spread",
        ["Past", "Present", "Future", "Problem", "Advice", "External Influences", "Outcome"]
    ),
    "astrological": (
        "Astrological Spread",
        ["Self", "Finances", "Communication", "Home & Family", "Creativity & Romance",
         "Work & Health", "Relationships", "Transformation", "Beliefs", "Career"]
    ),
    "career": (
        "Career Spread",
        ["Current Situation", "Strengths", "Weaknesses", "Opportunities", "Threats", "Future Path"]
    ),
    "shadow": ("Shadow Work Spread", ["Hidden Block", "Fear/Obstacle", "Lesson", "Action", "Growth", "Outcome"]),
    "year": (
        "Year Ahead Spread",
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    ),
    "elemental": ("Elemental Spread", ["Fire", "Water", "Air", "Earth"]),
    "chakra": ("Chakra Spread", ["Root", "Sacral", "Solar Plexus", "Heart", "Throat", "Third Eye", "Crown"]),
    "decision": ("Decision Spread", ["Situation", "Pros", "Cons", "Advice", "Outcome"]),
    "financial": ("Financial Spread", ["Current Situation", "Risks", "Opportunities", "Advice", "Outcome"]),
}

#util
def shuffle_deck(deck):
    """Shuffles the deck in place."""
    shuffle(deck)

def deal_cards(deck, number_of_cards):
    """Deals a number of cards from the deck."""
    if number_of_cards > len(deck):
        raise ValueError("Not enough cards in the deck to deal")
    return [deck.pop() for _ in range(number_of_cards)]

def get_minor_arcana_meaning(card):
    """Returns the meaning of a Minor Arcana card."""
    if " of " not in card:
        return "No description available."
    rank, suit = card.split(' of ') 
    return minor_arcana.get(suit, {}).get(rank, "No description available.")

def interpret_spread(cards, positions, title="Tarot Spread"):
    """
    Returns a structured interpretation of a tarot spread.
    Output: List of dicts with 'position', 'card', 'meaning'.
    """
    if len(cards) != len(positions):
        raise ValueError(f"{title} requires exactly {len(positions)} cards.")
    
    result = []
    for position, card in zip(positions, cards):
        if card in major_arcana:
            meaning = major_arcana[card]
        else:
            meaning = get_minor_arcana_meaning(card)
        result.append({"position": position, "card": card, "meaning": meaning})
    return result

def interpret_named_spread(name, cards):
    """Interprets a spread by its name."""
    if name not in SPREADS:
        raise ValueError(f"No spread named '{name}'")
    title, positions = SPREADS[name]
    return interpret_spread(cards, positions, title)
