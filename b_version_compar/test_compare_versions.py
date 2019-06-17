from versions import compare_versions

def test_first_less_than_second():
    assert compare_versions('1.2.3', '2.1.0') == "Version '1.2.3' is less than '2.1.0'"

def test_second_less_than_first():
    assert compare_versions('1.2.3', '0.1.0') == "Version '0.1.0' is less than '1.2.3'"

def test_one_value_vs_more_values():
    assert compare_versions('1', '2.1.0') == "Version '1' is less than '2.1.0'"
    assert compare_versions('1', '2.1') == "Version '1' is less than '2.1'"
    assert compare_versions('1.0', '2') == "Version '1.0' is less than '2'"

def test_first_minor_on_last_digit():
    assert compare_versions('1.0.9', '1.0.10') == "Version '1.0.9' is less than '1.0.10'"
    assert compare_versions('0.3', '0.4') == "Version '0.3' is less than '0.4'"
    assert compare_versions('1', '2') == "Version '1' is less than '2'"


def test_second_less_on_digit_two():
    assert compare_versions('1.3.1', '1.5.0') == "Version '1.3.1' is less than '1.5.0'"


def test_first_less_than_second():
    assert compare_versions('1.2.3', '2.1.0') == "Version '1.2.3' is less than '2.1.0'"

def test_first_less_than_second():
    assert compare_versions('1.2.3', '2.1.0') == "Version '1.2.3' is less than '2.1.0'"


def test_equal_vertions():
    assert compare_versions('1.2.3', '1.2.3') == "Version '1.2.3' is equal to '1.2.3'"
    assert compare_versions('0.1', '0.1.0') == "Version '0.1' is equal to '0.1.0'"
    assert compare_versions('1', '1.0.0') == "Version '1' is equal to '1.0.0'"
