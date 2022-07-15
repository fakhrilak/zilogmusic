from setuptools import setup, find_packages

setup(
 name="zilogmusic",
 version="1.0.0",
 description="this is zilog music player",
 author="fakhrilak",
 author_email="fakhrilak@zilog.tech",
 license="GNU",
 url="blogger.zilog.tech",
 packages=["zilogmusic","zilogmusic/controllers","zilogmusic/config"],
 entry_points={
 "console_scripts": [
 "zilogmusic=zilogmusic:main",
 ]
 },
)
