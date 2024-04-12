from setuptools import setup, find_packages

setup(
    name="py-discord-html-transcripts",
    version="1.0.0",
    author="FroostySnoowman",
    author_email="froostysnoowmanbusiness@gmail.com",
    description="A simple Discord chat exporter for Python Discord bots.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FroostySnoowman/py-discord-html-transcripts",
    packages=find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    license="GPL-3.0-only",
    python_requires=">=3.6",
    install_requires=[
        "aiohttp",
        "pytz",
        "grapheme",
        "emoji",
    ],
    keywords="chat exporter, discord chat exporter, discord, discordpy, disnake, pycord, nextcord",
)
