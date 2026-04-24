# Stellar Burgers — Unit Test Suite

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-7.4+-orange.svg)](https://docs.pytest.org/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://pytest-cov.readthedocs.io/)
[![Stellar Burgers](https://img.shields.io/badge/Stellar%20Burgers-Web%20App-FF6B6B)](https://stellarburgers.nomoreparties.site/)

Unit tests for the [Stellar Burgers](https://stellarburgers.education-services.ru/) application.  
The project covers core business logic classes with **100% code coverage**.

## Project Description

This project contains unit tests built with **pytest** for the Stellar Burgers burger constructor.  
It verifies the functionality of the `Bun`, `Burger`, `Ingredient`, and `Database` classes.  
The test suite includes:

- Adding/removing ingredients to/from the burger
- Calculating total price with different ingredient combinations
- Getting ingredient information
- Database availability checks and ingredient retrieval

> The project uses **mocks** and **parameterization** where appropriate to ensure complete and isolated unit testing.

## Test Coverage

- **`Bun` class** — name and price getters, immutability checks
- **`Ingredient` class** — type, name, price getters
- **`Burger` class** — ingredient management, price calculation, receipt generation
- **`Database` class** — availability checks, ingredient retrieval

All classes are covered with unit tests achieving **100% test coverage** (HTML coverage report available at `htmlcov/index.html`).

## Project Structure

Stellar-Burgers-Unit-Tests/
    ├── README.md
    ├── praktikum.py
    ├── requirements.txt
    ├── praktikum/
    │   ├── bun.py
    │   ├── burger.py
    │   ├── database.py
    │   ├── ingredient.py
    │   └── ingredient_types.py
    └── tests/
        └── burger_test.py

## Setup & Installation

### Requirements
- Python 3.12+
- pytest
- pytest-cov

### Installation

1. **Clone the repository**

```bash
   git clone https://github.com/nvbeznosova/Stellar-Burgers-Unit-Tests.git
   cd Stellar-Burgers-Unit-Tests
   ``` 

2. **Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# .venv\Scripts\activate    # On Windows
```  

3. **Install dependencies**

```bash
pip install -r requirements.txt
``` 

### Running Tests

1. **Run all tests**

```bash
pytest tests/
``` 

2. **Run tests with coverage report**

```bash
pytest --cov=praktikum tests/
```

3. **Generate HTML coverage report**

```bash
pytest --cov=praktikum --cov-report=html tests/
```

The HTML report will be available at htmlcov/index.html

