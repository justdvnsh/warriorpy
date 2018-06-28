from setuptools import setup, find_packages


setup(
    name='Warrior-pytho-3',
    version='0.0.1',
    packages=['warriorpy', 'warriorpy.towers.beginner', 'warriorpy.towers.intermediate','warriorpy.warriorpyAbilities.src', 'warriorpy.warriorpyCli.src', 'warriorpy.warriorpyCli.src.ui', 'warriorpy.warriorpyCli.templates' ,'warriorpy.warriorpyCore.src', 'warriorpy.warriorpyGeography.src', 'warriorpy.warriorpyUnits.src'],
    packages_dir={'warriorpy': 'warriorpy'},
    scripts=['bin/warriorpy.py'],
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
