from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os, sys


# From here: http://pytest.org/2.2.4/goodpractises.html
class RunTests(TestCommand):
    DIRECTORY = 'test'

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [self.DIRECTORY]
        self.test_suite = True

    def run_tests(self):
        # Import here, because outside the eggs aren't loaded.
        import pytest
        errno = pytest.main(self.test_args)
        if errno:
            raise SystemExit(errno)


NAME = 'streamy'
OWNER = 'timedata-org'
FILENAME = os.path.join(os.path.dirname(__file__), 'VERSION')
VERSION = open(FILENAME).read().strip()

URL = 'http://github.com/{OWNER}/{NAME}'.format(**locals())
DOWNLOAD_URL = '{URL}/archive/{VERSION}.tar.gz'.format(**locals())


setup(
    name='stream',
    version=VERSION,
    description=('streamy splits a stream into a stream of strings that are'
                 ' complete JSON expressions'),
    author='Tom Ritchford',
    author_email='tom@swirly.com',
    url=URL,
    download_url=DOWNLOAD_URL,
    license='MIT',
    packages=find_packages(exclude=['test']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    tests_require=[],
    cmdclass={'test': RunTests},
    keywords=['git', 'import'],
    include_package_data=True,
    install_requires=[],
)
