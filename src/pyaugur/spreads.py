"""
Predefined Tarot spreads and spread interpretation functions.
Works on desktop and MicroPython.
"""

SPREADS = {
    "one_card": ("One-Card Daily Draw", ["Daily Guidance"]),
    "two_card": ("Two-Card Choice", ["Option A", "Option B"]),
    "three_card": ("Three-Card Spread", ["Past", "Present", "Future"]),
    "relationship": (
        "Relationship Spread",
        [
            "Your Feelings",
            "Their Feelings",
            "Current State",
            "Strengths",
            "Challenges",
            "Potential Outcome",
        ],
    ),
    "celtic_cross": (
        "Celtic Cross Spread",
        [
            "The Present",
            "The Challenge",
            "The Past",
            "The Future",
            "The Above",
            "The Below",
            "The Self",
            "The Environment",
            "The Hopes and Fears",
            "The Outcome",
        ],
    ),
    "horseshoe": (
        "Horseshoe Spread",
        [
            "Past",
            "Present",
            "Future",
            "Problem",
            "Advice",
            "External Influences",
            "Outcome",
        ],
    ),
    "astrological": (
        "Astrological Spread",
        [
            "Self",
            "Finances",
            "Communication",
            "Home & Family",
            "Creativity & Romance",
            "Work & Health",
            "Relationships",
            "Transformation",
            "Beliefs",
            "Career",
        ],
    ),
    "career": (
        "Career Spread",
        [
            "Current Situation",
            "Strengths",
            "Weaknesses",
            "Opportunities",
            "Threats",
            "Future Path",
        ],
    ),
    "shadow": (
        "Shadow Work Spread",
        ["Hidden Block", "Fear/Obstacle", "Lesson", "Action", "Growth", "Outcome"],
    ),
    "year": (
        "Year Ahead Spread",
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
    ),
    "elemental": ("Elemental Spread", ["Fire", "Water", "Air", "Earth"]),
    "chakra": (
        "Chakra Spread",
        ["Root", "Sacral", "Solar Plexus", "Heart", "Throat", "Third Eye", "Crown"],
    ),
    "decision": ("Decision Spread", ["Situation", "Pros", "Cons", "Advice", "Outcome"]),
    "financial": (
        "Financial Spread",
        ["Current Situation", "Risks", "Opportunities", "Advice", "Outcome"],
    ),
}


def interpret_named_spread(name, cards, meanings):
    """
    Interpret a named spread.
    Args:
        name (str): The spread key in SPREADS.
        cards (list): Cards dealt in order.
        meanings (dict): Dictionary of card -> meaning.
    Returns:
        list of dicts: Each dict has 'position', 'card', 'meaning'.
    """
    if name not in SPREADS:
        raise ValueError(f"No spread named '{name}'")

    title, positions = SPREADS[name]
    if len(cards) != len(positions):
        raise ValueError(f"Spread '{name}' requires {len(positions)} cards.")

    result = []
    for pos, card in zip(positions, cards):
        meaning = meanings.get(card, "No description available.")
        result.append(
            {
                "position": pos,
                "card": card,
                "meaning": meaning,
            }
        )
    return result
