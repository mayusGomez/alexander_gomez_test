import pytest

from versions import convert_to_sw_version, compare_versions
from versions.exceptions import WrongVersionException


def test_convert_to_version_three_position():
    assert convert_to_sw_version('1.3.4') == [1,3,4]
    assert convert_to_sw_version('0.1.0') == [0,1,0]
    assert convert_to_sw_version('0.0.0') == [0,0,0]
    assert convert_to_sw_version('5.3.4') == [5,3,4]


def test_convert_to_version_two_positions():
    assert convert_to_sw_version('1.2') == [1,2,0]
    assert convert_to_sw_version('3.1') == [3,1,0]
    assert convert_to_sw_version('2.0') == [2,0,0]

def test_convert_to_version_one_positions():
    assert convert_to_sw_version('1') == [1,0,0]
    assert convert_to_sw_version('3') == [3,0,0]
    assert convert_to_sw_version('2') == [2,0,0]

def test_convert_to_version_three_position_colon():
    with pytest.raises(ValueError):
        convert_to_sw_version('1,3.4')

    with pytest.raises(ValueError):
        convert_to_sw_version('1.3,4')

    with pytest.raises(ValueError):
        convert_to_sw_version('1,3,4')


def test_convert_to_version_empty_with_points():
    with pytest.raises(ValueError):
        convert_to_sw_version('..')

    with pytest.raises(ValueError):
        convert_to_sw_version('0.1.')

    with pytest.raises(ValueError):
        convert_to_sw_version('.1.')

    with pytest.raises(ValueError):
        convert_to_sw_version('..0')    


def test_convert_to_version_three_position_not_numeric():
    with pytest.raises(ValueError):
        convert_to_sw_version('a.3.4')

    with pytest.raises(ValueError):
        convert_to_sw_version('a.b.4')

    with pytest.raises(ValueError):
        convert_to_sw_version('a.3.c')

    with pytest.raises(ValueError):
        convert_to_sw_version('a.b.c')

    with pytest.raises(ValueError):
        convert_to_sw_version('a.@.c')


def test_convert_to_version_empty_without_points():
    with pytest.raises(WrongVersionException):
        convert_to_sw_version('')


def test_convert_to_version_add_to_final_string():
    with pytest.raises(ValueError):
        convert_to_sw_version('1.3.4rc4')

    with pytest.raises(ValueError):
        convert_to_sw_version('1.3.4b0')

    with pytest.raises(ValueError):
        convert_to_sw_version('1.3.4a1')


def test_convert_to_version_negative_values():
    with pytest.raises(WrongVersionException):
        convert_to_sw_version('-1.0.0')

    with pytest.raises(WrongVersionException):
        convert_to_sw_version('-1.0.-1')

    with pytest.raises(WrongVersionException):
        convert_to_sw_version('-1.-1.0')

    with pytest.raises(WrongVersionException):
        convert_to_sw_version('-1.-2.-3')

