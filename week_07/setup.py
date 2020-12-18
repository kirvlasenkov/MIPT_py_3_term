import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mydearmath",  # Replace with your own username
    version="0.0.1",
    author="Kirill Vlasenkov",
    author_email="kirill.vlasenckov@gmail.com",
    description="A small example package, just for test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vlasenckov/MIPT_py_3_term",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
