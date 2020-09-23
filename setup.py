import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='sudoku9',
    version='0.1',
    scripts=['sudoku9'],
    author="Kunal Kumar",
    author_email="kkunal654@gmail.com",
    description="Python program to solve a Sudoku puzzle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kunalsingh2904/sudoku9",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
