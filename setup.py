from distutils.core import setup

files = ["entrycounter/*"]

setup(name="EntryCounter",
      version="0.0.1",
      author="Başar Noyan",
      author_email="basarnoyan1@gmail.com",
      packages=['entrycounter'],
      install_requires=[
          'imutils',
          'shapely',
          'grequests',
          'imutils',
          'configparser',
          'picamera[array]'
      ],
      scripts=['bin/entrycounter'])
