from distutils.core import setup

setup(
    name = "pygooglevoice",
    version = '0.5',
    url = 'http://code.google.com/p/pygooglevoice',
    author = 'Justin Quick and Joe McCall',
    author_email='justquick@gmail.com, joe@mcc4ll.us',
    description = 'Python 2/3 Interface for Google Voice',
    long_description = open('README.md').read(),
    packages = ['googlevoice'],
    scripts = ['bin/gvoice','bin/asterisk-gvoice-setup', 'bin/gvi']
)