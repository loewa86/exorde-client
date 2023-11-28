from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="exorde",
    version="v2.5.2",
    author="Exorde Labs",
    author_email="hello@exordelabs.com",
    description="The AI-based client to mine data and power the Exorde Network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loewa86/exorde-client",
    entry_points={"console_scripts": ["exorde = exorde.main:run"]},
    packages=find_packages(include=["exorde"]),
    include_package_data=True,

    python_requires=">=3.10",
)
