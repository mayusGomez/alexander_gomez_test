from versions.exceptions import WrongVersionException


def convert_to_sw_version(version=''):
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



def compare_versions():
    pass
