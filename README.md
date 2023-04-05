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

## Local Setup

The core of Eternity, located in `src` directory, is implemented in vanilla python and can be used as is.

To run the user interface and tests you will need to install the dependencies outlined in [requirements.txt](requirements.txt). For convenience, you can use Python's `venv` package to install dependencies in a virtual environment. You can find the instructions on creating and activating a virtual environment in the official [documentation](https://docs.python.org/3.10/library/venv.html). After setting up and activating your environment, you can install the dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

### UI

The web-based user interface developed in Flask can be located in `ui` directory. To run the UI, move to the `ui` directory by running the following command in your terminal:

```bash
cd ui
```

You can then launch the UI application by running the follwoing by running the following command in your terminal:

```bash
flask run
```

If the UI starts with no issues, you should see a set of outputs similar to the one below in your terminal:

```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

As the last output mentions, you can now access the UI app at http://127.0.0.1:5000/.

### Testing

Eternity utilizes [pytest]() framework for testing.
A set of unit-tests, located in `tests` directory, were implemented for Eternity core modules.

You can run all the tests by executing the following command in your terminal:

```bash
pytest tests
```

or run individual tests (e.g., unit-test for standard_deviation.py module) by executing the following command in your terminal:

```bash
pytest tests/test_standard_deviation.py
```

## License

Eternity is licensed under the terms of the [MIT License](LICENSE).
