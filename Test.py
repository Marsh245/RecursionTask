import pytest 
from io import StringIO
import sys
from TaskPython import printNumbers


def test_print_numbers(capsys):
    expected_output = '12345'
    printNumbers(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_print_twenty(capsys):
    expected_output ='1234567891011121314151617181920'
    printNumbers(20)
    captured = capsys.readouterr()
    assert captured.out == expected_output



