from pyaugur import (
    build_deck,
    shuffle_deck,
    deal_cards,
    deal_cards_reversals,
    interpret_spread,
    interpret_named_spread,
    SPREADS,
    ALL_MEANINGS,
)


# Use a fresh deck for each test
def test_deck_has_78_cards():
    deck = build_deck()
    assert len(deck) == 78


def test_shuffle_deck_preserves_cards():
    deck = build_deck()
    shuffled = deck[:]
    shuffle_deck(shuffled)

    # order may change, contents must not
    assert set(deck) == set(shuffled)


def test_deal_cards_reduces_deck_size():
    deck = build_deck()
    shuffle_deck(deck)
    hand = deal_cards(deck, 3)

    assert len(hand) == 3
    assert len(deck) == 75


def test_deal_cards_not_enough_cards():
    deck = ["The Fool"]
    raised = False
    try:
        deal_cards(deck, 2)
    except ValueError:
        raised = True

    assert raised


def test_get_minor_arcana_meaning_valid():
    meaning = ALL_MEANINGS["Ace of Cups"]
    assert meaning is not None
    assert isinstance(meaning, str)


def test_get_minor_arcana_meaning_invalid():
    meaning = ALL_MEANINGS.get("Nonexistent Card", "No description available.")
    assert meaning == "No description available."


def test_interpret_spread_major_and_minor():
    cards = ["The Fool", "Ace of Cups"]
    positions = ["Past", "Present"]

    result = interpret_spread(cards, positions, ALL_MEANINGS)

    assert len(result) == 2
    assert result[0]["meaning"] == ALL_MEANINGS["The Fool"]
    assert result[1]["meaning"] == ALL_MEANINGS["Ace of Cups"]


def test_interpret_spread_wrong_card_count():
    cards = ["The Fool"]
    positions = ["Past", "Present"]

    raised = False
    try:
        interpret_spread(cards, positions, ALL_MEANINGS)
    except ValueError:
        raised = True

    assert raised


def test_interpret_named_spread_valid():
    deck = build_deck()
    shuffle_deck(deck)

    title, positions = SPREADS["three_card"]
    cards = deal_cards(deck, len(positions))

    result = interpret_named_spread("three_card", cards, ALL_MEANINGS)

    assert len(result) == len(positions)
    for r in result:
        assert "position" in r
        assert "card" in r
        assert "meaning" in r


def test_interpret_named_spread_invalid():
    raised = False
    try:
        interpret_named_spread("not_a_real_spread", [], ALL_MEANINGS)
    except ValueError:
        raised = True

    assert raised


def test_deal_cards_with_reversals():
    deck = build_deck()
    cards = deal_cards_reversals(deck, 5, reversal_chance=1.0)  # all reversed
    assert all(c["reversed"] is True for c in cards)

    cards = deal_cards_reversals(deck, 5, reversal_chance=0.0)  # none reversed
    assert all(c["reversed"] is False for c in cards)


def run_all_tests():
    tests = [
        test_deck_has_78_cards,
        test_shuffle_deck_preserves_cards,
        test_deal_cards_reduces_deck_size,
        test_deal_cards_not_enough_cards,
        test_get_minor_arcana_meaning_valid,
        test_get_minor_arcana_meaning_invalid,
        test_interpret_spread_major_and_minor,
        test_interpret_spread_wrong_card_count,
        test_interpret_named_spread_valid,
        test_interpret_named_spread_invalid,
        test_deal_cards_with_reversals,
    ]

    for test in tests:
        test()
        print("PASS:", test.__name__)

    print("\nAll tests passed ✨")


if __name__ == "__main__":
    run_all_tests()
