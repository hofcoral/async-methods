from setuptools import setup

setup(
    name="async-methods",
    version="0.1.0",
    description="Simple lightweight library for async methods like intervals and timeouts.",
    url="https://hofcoral/async-methods",
    author="Hof Coral",
    author_email="hofcoral@gmail.com",
    license="MIT License",
    packages=["async_methods"],
    requires=["threading"],
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Software Distribution",
        "Topic :: Utilities",
    ],
)
