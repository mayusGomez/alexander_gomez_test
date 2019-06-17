import pytest 

from lines.line import XLine
from lines.exception import WrongValuesException


def test_first_minor_line_without_overlap():
    line_one = XLine(1,5)
    line_two = XLine(7,8)

    assert line_one.detect_overlap(line_two) == False
    assert line_two.detect_overlap(line_one) == False


def test_second_minor_line_without_overlap():
    line_one = XLine(7,10)
    line_two = XLine(1,4)

    assert line_one.detect_overlap(line_two) == False
    assert line_two.detect_overlap(line_one) == False


def test_first_minor_line_without_overlap_start_close():
    line_one = XLine(1,6)
    line_two = XLine(6,8)

    assert line_one.detect_overlap(line_two) == False
    assert line_two.detect_overlap(line_one) == False


def test_first_minor_line_with_overlap():
    line_one = XLine(1,6)
    line_two = XLine(5,8)

    assert line_one.detect_overlap(line_two) == True
    assert line_two.detect_overlap(line_one) == True


def test_second_minor_line_with_overlap():
    line_one = XLine(6,12)
    line_two = XLine(1,10)

    assert line_one.detect_overlap(line_two) == True
    assert line_two.detect_overlap(line_one) == True


def test_first_content_second_with_overlap():
    line_one = XLine(1,200)
    line_two = XLine(20,25)

    assert line_one.detect_overlap(line_two) == True
    assert line_two.detect_overlap(line_one) == True


def test_invalid_instance_line_two():
    line_one = XLine(1,200)
    line_two = {
        'a': 1,
        'b': 2
    }

    with pytest.raises(WrongValuesException):
        assert line_one.detect_overlap(line_two)



def test_negative_first_content_second_with_overlap():
    line_one = XLine(-100,200)
    line_two = XLine(20,25)

    assert line_one.detect_overlap(line_two) == True
    assert line_two.detect_overlap(line_one) == True


def test_character_validation():
    with pytest.raises(ValueError):
        line_two = XLine('a',25)


def test_point():
    with pytest.raises(WrongValuesException):
        line_one = XLine(1,1)
        

def test_x2_minor_than_x1():
    with pytest.raises(WrongValuesException):
        line_one = XLine(5,1)
