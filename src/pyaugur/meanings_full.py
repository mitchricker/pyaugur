"""
Full Tarot card meanings for desktop (CPython).
Includes detailed interpretations for Major and Minor Arcana.
"""

# Major Arcana: full descriptions
MAJOR_MEANINGS = {
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
    "The World": "Completion, achievement, and fulfillment.",
}

# Minor Arcana: full descriptive phrases
MINOR_MEANINGS = {
    # Wands
    "Ace of Wands": "New beginnings, potential, and inspiration.",
    "2 of Wands": "Planning, decisions, and progress.",
    "3 of Wands": "Expansion, foresight, and leadership.",
    "4 of Wands": "Stability, celebration, and harmony.",
    "5 of Wands": "Conflict, competition, and challenge.",
    "6 of Wands": "Victory, success, and recognition.",
    "7 of Wands": "Perseverance, defense, and determination.",
    "8 of Wands": "Movement, action, and swift progress.",
    "9 of Wands": "Resilience, courage, and perseverance.",
    "10 of Wands": "Burden, responsibility, and completion.",
    "Page of Wands": "Enthusiasm, exploration, and creativity.",
    "Knight of Wands": "Action, adventure, and ambition.",
    "Queen of Wands": "Leadership, vision, and passion.",
    "King of Wands": "Authority, control, and mastery.",
    # Cups
    "Ace of Cups": "Emotional fulfillment, new relationships, and love.",
    "2 of Cups": "Partnership, union, and harmony.",
    "3 of Cups": "Joy, celebration, and friendship.",
    "4 of Cups": "Discontent, contemplation, and reevaluation.",
    "5 of Cups": "Loss, regret, and mourning.",
    "6 of Cups": "Nostalgia, memories, and reconnection.",
    "7 of Cups": "Choices, illusions, and fantasy.",
    "8 of Cups": "Leaving behind, moving on, and transition.",
    "9 of Cups": "Contentment, satisfaction, and wishes fulfilled.",
    "10 of Cups": "Emotional fulfillment, family, and happiness.",
    "Page of Cups": "Imagination, intuition, and emotional growth.",
    "Knight of Cups": "Romance, charm, and idealism.",
    "Queen of Cups": "Compassion, empathy, and emotional depth.",
    "King of Cups": "Emotional control, authority, and leadership.",
    # Swords
    "Ace of Swords": "Clarity, truth, and new ideas.",
    "2 of Swords": "Indecision, choices, and balance.",
    "3 of Swords": "Heartbreak, sorrow, and separation.",
    "4 of Swords": "Rest, recovery, and contemplation.",
    "5 of Swords": "Conflict, loss, and strategy.",
    "6 of Swords": "Transition, moving on, and relief.",
    "7 of Swords": "Deception, strategy, and betrayal.",
    "8 of Swords": "Restriction, limitation, and mental anguish.",
    "9 of Swords": "Anxiety, worry, and sleeplessness.",
    "10 of Swords": "Endings, betrayal, and crisis.",
    "Page of Swords": "Curiosity, intellect, and vigilance.",
    "Knight of Swords": "Action, conflict, and decisiveness.",
    "Queen of Swords": "Intellect, independence, and perception.",
    "King of Swords": "Authority, intellect, and strategic thinking.",
    # Pentacles
    "Ace of Pentacles": "Opportunity, prosperity, and manifestation.",
    "2 of Pentacles": "Balance, adaptability, and multitasking.",
    "3 of Pentacles": "Collaboration, skill, and mastery.",
    "4 of Pentacles": "Stability, security, and possessiveness.",
    "5 of Pentacles": "Financial loss, insecurity, and struggle.",
    "6 of Pentacles": "Generosity, giving, and receiving.",
    "7 of Pentacles": "Patience, evaluation, and growth.",
    "8 of Pentacles": "Diligence, hard work, and skill development.",
    "9 of Pentacles": "Abundance, self-sufficiency, and luxury.",
    "10 of Pentacles": "Wealth, family, and legacy.",
    "Page of Pentacles": "Studiousness, ambition, and potential.",
    "Knight of Pentacles": "Practicality, dedication, and responsibility.",
    "Queen of Pentacles": "Nurturing, practicality, and resourcefulness.",
    "King of Pentacles": "Success, control, and financial acumen.",
}

# Combine all into one dictionary
ALL_MEANINGS = {}
ALL_MEANINGS.update(MAJOR_MEANINGS)
ALL_MEANINGS.update(MINOR_MEANINGS)
