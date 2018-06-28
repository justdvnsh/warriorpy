from setuptools import setup, find_packages


setup(
    name='warriorpy',
    version='0.0.1',
    packages=find_packages(),
    package_data={'warriorpy': ['README']},
    scripts=['bin/warriorpy'],
    author="Divyansh Dwivedi",
    author_email="justdvnsh2208@gmail.com",
    description=("An exciting game of programming and Artificial Intelligence"),
    long_description=open('README.md').read(),
    install_requires=['jinja2'],
    license="MIT",
    url="https://github.com/justdvnsh/warriorpy",
    keywords="python ruby javascript rubywarrior warriorjs warriorpy",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)
