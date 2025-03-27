# API Test Automation Framework (Python)

Comprehensive API test automation for financial systems using Python, Pytest, and Allure. This project demonstrates modern API testing practices with CI/CD integration and professional reporting.


<p align="center">
  <a href="https://josinaldogjunior.github.io/python-automation-api-test/">
    <img src="https://img.shields.io/badge/Allure%20Report-View%20Live-brightgreen.svg" alt="View Live Report">
  </a>
</p>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Architectural Principles](#-key-architectural-principles)
- [Technology Stack](#-technology-stack)
- [Project Structure](#️-project-structure)
- [Getting Started](#-getting-started)
- [Running Tests & Viewing Reports](#-running-tests--viewing-reports)
- [CI/CD Pipeline](#-cicd-pipeline)

---

## 🔍 Overview
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Pytest-8-blue.svg?logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Requests-2-orange.svg" alt="Requests">
  <img src="https://img.shields.io/badge/Allure%20Report-2-orange.svg?logo=allure&logoColor=white" alt="Allure Report">
  <a href="https://github.com/JosinaldoGJunior/python-automation-api-test/actions/workflows/ci_cd_pipeline.yml">
    <img src="https://github.com/JosinaldoGJunior/python-automation-api-test/actions/workflows/ci_cd_pipeline.yml/badge.svg" alt="CI/CD Status">
  </a>
</p>
This framework is designed to provide comprehensive, reliable, and maintainable automated tests for a RESTful API. The architecture emphasizes a clear separation between the **reusable framework core** and the **tests themselves**, ensuring that the code is easy to read, debug, and scale as the application's feature set grows. It serves as a practical demonstration of modern Python API test automation techniques.

---

## 🌟 Key Architectural Principles

This project was built following industry-standard best practices and design patterns to ensure high quality.

* **API Client Pattern:** All direct API communication is encapsulated within dedicated `Client` classes (e.g., `AccountsClient`). This abstracts away the implementation details of the `requests` library, making tests cleaner and focused on business logic.

* **Separation of Concerns (SoC):** The project is organized into two distinct top-level packages:
    * `api_framework/`: Contains all the reusable "library" code (clients, configuration, utilities).
    * `tests/`: Contains only the test files and their specific configurations (`conftest.py`).

* **Dependency Injection with Pytest Fixtures:** The framework leverages `pytest`'s powerful fixture system to manage and inject dependencies. Clients, authentication headers, and test data are automatically created and provided to the tests that need them, promoting clean, decoupled test code.

* **Arrange-Act-Assert (AAA) Pattern:** Every test strictly follows the AAA structure, making its intent and flow universally readable and easy to understand.

* **Deterministic Test Data Factories:** The `payload_generator` module acts as a factory for creating predictable and specific test data (e.g., `generate_new_income_payload`), which is critical for writing reliable, non-flaky tests.

* **Scenario Builder for Preconditions:** A dedicated `scenario_builder` module provides high-level functions to create complex preconditions (e.g., an account that already has a transaction), keeping the `Arrange` block of tests simple and declarative.

---

## 🛠️ Technology Stack

| Category | Technologies Used |
| :--- | :--- |
| **Core Language** | Python 3.10+ |
| **Testing Framework** | Pytest |
| **HTTP Client** | Requests |
| **Assertions** | AssertPy |
| **Reporting** | Allure Framework |
| **CI/CD** | GitHub Actions |
| **Environment Mgmt** | python-dotenv |


---

## 🗂️ Project Structure

The framework is organized into a clean, professional structure that separates the framework code from the tests.

```
finance-api-tests/
├── api_framework/                  # The reusable framework code
│   ├── __init__.py
│   ├── clients/                    # API Client layer
│   │   ├── __init__.py
│   │   └── accounts_client.py
│   ├── core/                       # Core logic (auth, config)
│   │   ├── __init__.py
│   │   └── config.py
│   └── utils/                      # Test utilities
│       ├── __init__.py
│       ├── payload_generator.py
│       └── scenario_builder.py
├── tests/                          # The test suite
│   ├── __init__.py
│   ├── conftest.py                 # Central Pytest fixtures file
│   ├── test_accounts.py
│   └── test_transactions.py
├── .env.example                    # Example environment file
├── .gitignore
├── pytest.ini                      # Pytest configuration (e.g., markers)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* `pip` and `venv` (usually included with Python)
* Git

### Installation & Configuration

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/JosinaldoGJunior/python-automation-api-test.git](https://github.com/JosinaldoGJunior/python-automation-api-test.git)
    cd python-automation-api-test
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your environment variables:**
    * Create a file named `.env` in the project root.
    * Copy the contents from `.env.example` or use the template below and fill in your credentials.
    
    **`.env` template:**
    ```env
    # Credentials for authentication
    API_EMAIL=your-email@example.com
    API_PASSWORD=your-password
    
    # Target API URL
    BASE_URL=[https://barrigarest.wcaquino.me](https://barrigarest.wcaquino.me)
    ```

---

## ⚡ Running Tests & Viewing Reports

1.  **Run all tests:**
    ```bash
    pytest
    ```

2.  **Run tests by marker:**
    ```bash
    # Run only smoke tests
    pytest -m smoke

    # Run all tests except smoke tests
    pytest -m "not smoke"
    ```

3.  **Generate and serve the Allure report locally:**
    ```bash
    # Step 1: Run tests and generate allure results
    pytest --alluredir=allure-results

    # Step 2: Serve the generated report in a web browser
    allure serve allure-results
    ```

---

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** for continuous integration. The workflow automatically executes the entire test suite on every push and pull request to the `main` branch, generating and deploying a live Allure report to GitHub Pages.

➡️ **[View the Latest Live Report on GitHub Pages](https://josinaldogjunior.github.io/python-automation-api-test/)**

---

## 👤 Author

**Josinaldo Junior**

* **GitHub:** [@josinaldogjunior](https://github.com/josinaldogjunior)
* **LinkedIn:** `https://www.linkedin.com/in/josinaldo-junior/` ---

## 📄 License

This project is licensed under the MIT License.