#!/usr/bin/python

from distutils.core import setup

VERSION = open("version", "r+").read().split()[0]

setup(name="zmugjson",
      version="0.2",
      description="zmugjson a smugmug.com JSON api",
      long_description="A JSON-based api wrapper used to connect to smugmug.com",
      author="Jesus M. Rodriguez",
      author_email="jmrodri@nc.rr.com",
      url="http://zmugtools.sourceforge.net",
      py_modules=["zmugjson", "config"],
      license="GPL",
      data_files=[("/etc/zmugjson", ["logger.conf"]),
                  ("/usr/share/doc/zmugjson-%s" % VERSION, ["LICENSE.TXT"])
      ]
     )
