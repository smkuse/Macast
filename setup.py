"""
This is a setup.py script

"""

import os
import sys
from setuptools import setup, find_packages

VERSION = "0.0.0"
with open('macast/.version', 'r') as f:
    VERSION = f.read().strip()
LONG_DESCRIPTION = ""
with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
OPTIONS = {}
INSTALL = ["requests>=2.33.1", "appdirs>=1.4.4", "cherrypy>=18.10.0", "lxml>=6.1.0", "netifaces-plus>=0.11.0"]
PACKAGES = find_packages()

if sys.platform == 'darwin':
    INSTALL += ["rumps>=0.4.0",
                "pyperclip>=1.11.0"]
elif sys.platform == 'win32':
    INSTALL += ["pillow>=12.2.0",
                "pyperclip>=1.11.0",
                "pystray>=0.19.5"]
else:
    INSTALL += ["pillow>=12.2.0",
                "pystray @ git+https://github.com/xfangfang/pystray.git",
                "pyperclip @ git+https://github.com/xfangfang/pyperclip.git"]

setup(
    name="macast",
    version=VERSION,
    author="xfangfang",
    author_email="xfangfang@126.com",
    description="a DLNA Media Renderer",
    license="GPL3",
    url="https://github.com/xfangfang/Macast",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=["Topic :: Multimedia :: Sound/Audio",
                 "Topic :: Multimedia :: Video",
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.10',
                 'Programming Language :: Python :: 3.11',
                 'Programming Language :: Python :: 3.12',
                 'Programming Language :: Python :: 3.13',
                 'Programming Language :: Python :: 3.14',
                 'Operating System :: MacOS :: MacOS X',
                 ],
    platforms=["MacOS X"],
    keywords=["mpv", "dlna", "renderer"],
    options=OPTIONS,
    install_requires=INSTALL,
    packages=PACKAGES,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'macast-cli = macast.macast:cli',
            'macast-gui = macast.macast:gui'
        ]
    },
    python_requires=">=3.10",
)
