# Eternity

A scientific calculator developed in python that offers a web-based user interface implemented using [Flask](https://flask.palletsprojects.com/en/2.2.x/).

## Development

Development process of Eternity included various elements of Agile methodology including:

- Conducting interviews with potential users
- Creating personas for potential users
- Gathering use cases based on analysis of interviews and personas
- Documenting functionalities
- Creating Class Responsability Collborator (CRC) models

along common software development practices such as testing, debugging, and code reviewing.

## Instructions for running the unit tests

In order to run the unit tests you will need to install pytest.

To install pytest using pip package installer and terminal:

`pip install pytest`

Before running the pytest command to execute the tests make sure you are in the eternity main directory.

To run all tests:

`pytest deliverable3/tests`

To run individual tests:

`pytest deliverable3/tests/name_of_test_file`

For example to run unit test for standard deviation module:

`pytest deliverable3/tests/test_standard_deviation.py`
