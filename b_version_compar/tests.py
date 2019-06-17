from versions import convert_to_sw_version, compare_versions


def test_convert_to_version_three_position():
    assert convert_to_sw_version('1.3.4') == [1,3,4]



'''
def test_first_less_than_second():
    assert convert_to_sw_version('1.2.3', '2.1.0') == "Version '1.2.3' is less than '2.1.0'"
'''