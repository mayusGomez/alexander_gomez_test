import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='versions',
    version='1.0.0',
    license='GNU',
    maintainer='Alexander Gomez',
    maintainer_email='alexander.gomez.higuita@gmail.com',
    description='Funtionalities for software versions',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'test': [
            'pytest'
        ],
    },
)