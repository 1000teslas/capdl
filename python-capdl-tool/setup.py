import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="capdl",
    version="0.2.1-dev",
    author="Gerwin Klein",
    author_email="gerwin.klein@proofcraft.systems",
    description="A Python module for providing CapDL support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.sel4.systems/projects/capdl/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=["capdl"],
    python_requires=">=3.9",
)
