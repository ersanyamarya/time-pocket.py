import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timepocket",  # Replace with your own username
    version="0.0.1",
    author="Sanyam Arya",
    author_email="er.sanyam.arya@gmail.com",
    description="Some simple time utilities which you can have with you while developing in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/ersanyamarya/timepocket",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.6',
)
