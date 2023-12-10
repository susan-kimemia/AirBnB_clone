# Welcome!

Welcome to our AirBnB Console Prototype project! This console application allows you to create and manage objects related to an Airbnb-like system through simple commands.

## Project Overview
1. [Features](#features)
2. [Installation](#installation)
3. [How to Use](#how-to-use)
4. [Contributing](#contributing)
5. [License](#license)

## Getting Started

## Features
* Object creation and manipulation through the console
* Storage

## Installation
1. Clone the repository to your local machine
`git clone https://github.com/chimaskyy/AirBnB_clone`

## How to Use
1. Navigate to the repository directory
`cd AirBnB_clone`
2. run `./console.py`

## Examples
1. Interactive mode execution:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

2. non-interactive mode execution:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$


All tests should also pass in non-interactive mode:
$ echo "python3 -m unittest discover tests" | bash
