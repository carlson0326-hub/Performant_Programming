from setuptools import setup

setup(
    name='Django Quiz App',
    version='1',
    packages=['app','SemesterProj','static','templates','accounts','quiz'],
    description='Sprint 1 of the Quiz App',
    install_requires=['Django'],

    entry_points =
    { 'console_scripts':
        [
            'runmyserver = app.run:main',
            'initmyserver = app.init:main',
        ]
    },
)