#!/usr/bin/env python3
""" A rudimentary password strength tester """

import sys
import re

def test_password(password):
    """ test the given password """
    long_enough = len(password) >= 8
    has_upper = re.compile(r'[A-Z]').search(password) is not None
    has_lower = re.compile(r'[a-z]').search(password) is not None
    has_digit = re.compile(r'\d').search(password) is not None

    if not long_enough:
        print('Your password needs to be at least 8 characters long')
    if not has_upper:
        print('Your password needs an upper case character')
    if not has_lower:
        print('Your password needs a lower case character')
    if not has_digit:
        print('Your password needs a digit')
    if long_enough and has_upper and has_lower and has_digit:
        print('Your password is ok.')

test_password(sys.argv[1])
