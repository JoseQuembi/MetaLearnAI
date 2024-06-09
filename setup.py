from setuptools import setup, find_packages

setup(
    name="MetaLearnAI",
    version="0.1.0",
    author="José Quembi",
    author_email="josequembi@gmail.com",
    description="A Python library for implementing meta-learning algorithms.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/josequembi/MetaLearnAI",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "mealpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
