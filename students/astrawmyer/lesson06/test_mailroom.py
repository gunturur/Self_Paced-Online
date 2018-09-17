#!/usr/bin/env python3

import mailroom as m
import pytest
import sys


def test_display_list(capsys):
    result = m.display_list()
    out, err = capsys.readouterr()
    assert out == "Manny Machado\nAdam Jones\nChris Davis\n"

def test_write_letter():
    expected = "Dear Manny,\nThank you for donating $8.00 to the Human Fund. " \
            "Your money will be used appropriately."
    assert m.write_letter("Manny",8) == expected

def test_write_report(capsys):
    expected_1 = 'Donor Name                | Total Given | Num Gifts | Average Gift\n'
    expected_2 = '-------------------------------------------------------------------\n'
    expected_3 = 'Adam Jones                 $    1369.80           3  $      456.60\n'
    expected = expected_1 + expected_2 + expected_3
    report_input = [[1369.80,'Adam Jones',3,456.60]]
    result = m.write_report(report_input)
    out, err = capsys.readouterr()
    assert out == expected


def test_thank_you_add_donation():
    input_val = ["Manny Machado", 2131]
    def mock_input(s):
        return input_val.pop(0)
    m.input = mock_input
    m.thank_you()
    assert m.ddonors == {"Manny Machado": [12.2,2.51,3.20,2131], "Adam Jones": [1024.14,22.21,323.45], "Chris Davis": [3.2,5.55,4.20]}
    
""" def test_thank_you_add_donation(capsys):
    m.input = 'list'
    m.thank_you() """

