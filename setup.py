import multiprocessing
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
import iic4sem

setup(
    name='IIC4Sem',
    version=iic4sem.__version__,
    packages=find_packages(exclude=['*.pyc']),
    scripts=['bin/iic4sem'],
    url="https://iic.ac.in",
    license='GPL 2',
    author="Abhinav Saxena",
    author_email="abhinav.saxena@iic.ac.in",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Networking",
    ],
    keywords="IIC UDSC",
    include_package_data=True,
    long_description=open('README.md').read(),
    description="""Basic Network Programming Assignments For IIC, UDSC 4 Sem Final""",
    test_suite='nose.collector',
    tests_require="nose",
    install_requires=open('requirements.txt').read().splitlines(),
)
