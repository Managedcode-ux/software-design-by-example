from glob_lit import Lit, Either


def test_either_two_literals_first():
    # /{a,b}/ matches "a"
    assert Either(Lit("a"), Lit("b")).match("a")


def test_either_two_literals_not_both():
    # /{a,b}/ doesn't match "ab"
    assert not Either(Lit("a"), Lit("b")).match("ab")


def test_either_followed_by_literal_match():
    # /{a,b}/ matches "ab"
    assert Either(Lit("a"), Lit("b"), Lit("c")).match("ac")


def test_either_followed_by_literal_no_match():
    # /{a,b}c/ doesn't match "ax"
    assert not Either(Lit("a"), Lit("b"), Lit("c")).match("ax")
