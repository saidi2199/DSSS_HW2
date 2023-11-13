from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',
        ],
    },
    author='saidireddy',
    author_email='saidi.ranabothu@fau.de',
    description='A simple math quiz game',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Apache License',
        'Operating System :: OS Independent',
    ],
)