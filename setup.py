from setuptools import setup, find_packages


setup(
    name="HodolBot",
    version="1.0.0",
    description="A discord bot.",
    url="https://github.com/sqrtpi177/hodol-bot",
    author="sqrtpi177",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "discord",
        "pylint",
        "requests"
    ],
    python_requires=">=3.8.5",
)
