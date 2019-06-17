from versions.exceptions import WrongVersionException


def convert_to_sw_version(version=None):
    """
    convert_to_sw_version
    Accept a string version like '1.2', '1', '3.2.1' and return a versión list format.
    :param version: string version
    :return: list with three digits positions 
    """
    if version == '':
        raise WrongVersionException('Versión must have a value')

    version_resp = []
    try:
        version_resp = [ int(position) for position in version.split('.')]
    except ValueError:
        raise ValueError('Number versions must be separated by "." and mustb be integers')

    for pos in version_resp:
        if pos < 0:
            raise WrongVersionException("Version numbers must be positives")

    if len(version_resp) == 1: 
        return version_resp + [0, 0]
    elif len(version_resp) == 2:
        return version_resp + [0]
    elif len(version_resp) == 3:
        return version_resp
    else:
        raise WrongVersionException('Version must have a maximum of 3 values')


def compare_versions(version_a=None, version_b=None):
    """
    compare_versions
    accepts 2 version string as input and returns whether one is greater than, equal, or less than the other
    :return: possible three values: 
    - Version 'x.x.x' is less than 'y.y.y'
    - Version 'y.y.y' is less than 'x.x.x'
    - Version 'x.x.x' is equal to 'y.y.y'
    """
    response_text = "Version '{}' is equal to '{}'".format(version_a, version_b)
    converted_version_a = convert_to_sw_version(version_a)
    converted_version_b = convert_to_sw_version(version_b)

    for position in range(len(converted_version_a)):
        if converted_version_a < converted_version_b:
            response_text = "Version '{}' is less than '{}'".format(version_a, version_b)
            break
        elif converted_version_a > converted_version_b:
            response_text = "Version '{}' is less than '{}'".format(version_b, version_a)
            break
        
    return response_text
