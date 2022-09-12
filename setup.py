from setuptools import setup


setup(
    name='enotify',
    version='0.1',
    author='Daniil Tretyakov',
    description='Send telegram message on build end',
    project_urls={
        'Source Code': 'https://github.com/D-Tretyakov/compilation_notifier'
    },

    install_requires=[
        'requests',
        'platformdirs'
    ],

    package_dir={'':'src'},
    packages=['enotify'],

    entry_points={
        'console_scripts': [
            'enotify = enotify.cli:main',
        ]
    }

)