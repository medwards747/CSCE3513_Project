"""PIP installer for csce3513_project"""

from setuptools import setup, find_packages


def readme():
    """Get long description from README.md"""
    with open('README.md') as f:
        return f.read()


setup(
    name="CSCE 3513 Project",
    version="0.1.0",
    author="Matthew Edwards, Devin Harris, Luke Simmons, Anh Tran, Isaac Withrow",
    author_email="me004@uark.edu, dsh004@uark.edu, las041@uark.edu, anh.tran.edu@gmail.com, ijwithro@uark.edu",
    description="CSCE 3513 Laser Tag Project for Team 15.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/medwards747/CSCE3513_Project",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        "Programming Language :: Python :: 3 :: Only",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Environment :: GUI',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Topic :: Education',
    ],
    python_requires='>=3.9',
    platforms=[
        'Linux',
        'MacOS X',
        'Windows'
    ],
    license='Proprietary'
)
