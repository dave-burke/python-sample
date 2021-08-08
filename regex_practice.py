#!/usr/bin/env python3
""" Regular Expression practice """

import re

def test_commas():
    """ Identify numbers with proper commas """
    comma_regex = re.compile(r'^\d{1,3}(,\d{3})*$')

    for test in '42','1,234','6,368,745','12,34,567','1234':
        match = comma_regex.search(test)
        print(test, 'matches' if match is not None else 'does not match')

test_commas()

def test_nakamoto():
    """ Find the last name 'Nakamoto' """
    nakamoto_regex = re.compile(r'[A-Z][a-zA-Z]+ Nakamoto')

    tests = [
            'Satoshi Nakamoto',
            'Alice Nakamoto',
            'RoboCop Nakamoto',
            'satoshi Nakamoto',
            'Mr. Nakamoto',
            'Satoshi nakamoto',
    ]
    for test in tests:
        match = nakamoto_regex.search(test)
        print(test, 'matches' if match is not None else 'does not match')

test_nakamoto()

def test_phrases():
    """ Identify phrases that match a specific pattern """
    phrase_regex = re.compile(
            r'(Alice|Bob|carol) (eats|pets|throws) (apples|cats|baseballs)', re.IGNORECASE)

    tests = [
            'Alice eats apples.',
            'Bob pets cats.',
            'Carol throws baseballs.',
            'BOB EATS CATS.',
            'RoboCop eats apples.',
            'ALICE THROWS FOOTBALLS.',
            'Carol eats 7 cats.',
    ]
    for test in tests:
        match = phrase_regex.search(test)
        print(test, 'matches' if match is not None else 'does not match')

test_phrases()
