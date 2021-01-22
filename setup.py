"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages
try:
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req.req_file import parse_requirements

try:  # pip >= 10
    from pip._internal.download import PipSession
except ImportError:  # pip <= 9.0.3
    from pip.download import PipSession

    def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: str
        The filename containing the requirements

    """

    install_reqs = parse_requirements(filename=source, session=PipSession())

    return [str(ir.req) for ir in install_reqs]


setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements/requirements.txt')
)


