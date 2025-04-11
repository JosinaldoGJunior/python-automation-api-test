
# 🏆 Automated Finance API Testing Suite
Comprehensive API test automation for financial systems using Python, Pytest, and Allure. This project demonstrates modern API testing practices with CI/CD integration and professional reporting.

## 📑 Table of Contents

- [Overview](#overview)
- [Reports](#reports)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Requirements](#requirements)
- [Installation and Execution](#installation-and-execution)
- [Configuration](#configuration)
- [CI/CD Pipeline](#cicd-pipeline)
- [Author](#author)
- [License](#license)

## 🔍 Overview

This project provides automated API testing for financial systems, covering:
- Authentication workflows
- Account management
- Transaction processing
- Data validation

Built with scalability in mind, it implements:
- Modular test architecture
- Secure credential management
- Comprehensive reporting
- CI/CD automation

## 📊 Reports

Allure reports are automatically generated after test runs. You can access them in two ways:

1. **Locally**: After running tests with `npm run allure:open`
2. **Online**: Visit the ➡️ <a href="https://josinaldogjunior.github.io/python-automation-api-test/" target="_blank">GitHub Pages</a> for the latest reports from CI/CD pipeline.




## ⚡ Features 

### 📖 **Complete API Coverage**
- **End-to-End Workflows**:  
  ✅ Authentication → Account Setup → Transactions  
  ✅ Data validation across all financial operations  

### 🧩 **Advanced Features**  
- **Test Framework**:  
  🐍 Pytest fixtures for test abstraction  
  🧹 Automatic test data cleanup  
  📌 Centralized test configuration (`conftest.py`)  
- **Validation**:  
  ✨ AssertPy for human-readable assertions  
  🛡️ Pydantic models for type-safe responses  

### 📊 **Smart Reporting**  
- **Allure Framework Integration**:  
  🔍 Detailed request/response logging  
  📸 Capture on failures (via pytest hooks)  
- **Hosting Solutions**:  
  🌐 GitHub Pages auto-deployment  
  📦 Artifact storage for CI failures  

### ⚡ **CI/CD Ready**  
- **GitHub Actions**:  
  🛠️ Parallel test execution  
  🔄 Scheduled runs (cron jobs)  
  ⚙️ Configurable test matrices  
- **Advanced Triggers**:  
  🎯 Path-based execution (only run affected tests)  
  🔒 Secret management for API credentials  

## 🗒️ Project Structure
```
finance-api-tests
├── .github
│   └── workflows
│       └── ci_cd_pipeline.yml
├── .venv
├── allure-results
├── core
│   ├── __init__.py
│   ├── auth.py
│   ├── base_test.py
│   ├── config.py
│   ├── payload.py
├── tests
│   ├── account
│   │   ├── __init__.py
│   │   └── test_account.py
│   ├── auth
│   │   ├── __init__.py
│   │   └── test_auth.py
│   ├── transaction
│   │   ├── __init__.py
│   │   └── test_transaction.py
├── .env
├── .gitignore
├── pytest.ini
├── requirements.txt
```

## 🛠️ Technology Stack

| Category       | Technologies                          |
|----------------|---------------------------------------|
| Core           | Python 3.10+, Pytest                 |
| HTTP           | Requests, HTTPX                      |
| Validation     | Pydantic, AssertPy                   |
| Reporting      | Allure Framework                     |
| Infrastructure | GitHub Actions, Docker               |
| Quality        | Pylint, Black, Mypy                  |


## 📋 Requirements

- Python 3.10+
- pip 22.3+
- Allure 2.13+
- Git 2.35+

## 🚀 Installation and Execution
###  **Clone the Repository**
```
git clone git@github.com:JosinaldoGJunior/python-automation-api-test.git
```
###  **Install Dependencies**
```
pip install -r requirements.txt
```
### Basic Execution
```bash
pytest tests/ --alluredir=allure-results
```

### With Report Generation
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results  # Local report
```

### Targeted Execution
```bash
# Run smoke tests only
pytest -m smoke

# Run specific module
pytest tests/account/

# Run with verbose output
pytest -v
```

## ⚙️ Configuration

1. Create a `.env` file in the project root with the following variables:
   ```
   API_EMAIL=your-email@example.com
   API_PASSWORD=your-password
   BASE_URL=https://barrigareact.wcaquino.me/
   API_LOGIN_URL=http://barrigarest.wcaquino.me/signin
   ```
⚠️ Security Note: Never commit sensitive data. The .env file is already in .gitignore.


## 🔄 CI/CD Pipeline

The GitHub Actions workflow provides:
- Triggered on push/PR to main
- Parallel test execution
- Allure report publishing
- Artifact storage for failures

Secrets Required:
- `API_EMAIL`:  Your email
- `API_PASSWORD`:  Your password
- `BASE_URL`: https://barrigareact.wcaquino.me/
- `API_LOGIN_URL`: http://barrigarest.wcaquino.me/signin

  

## 👤 Author
Created and maintained by [Josinaldo Junior](https://github.com/josinaldogjunior)


## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---
Feel free to reach out for questions, improvements, or collaboration opportunities. 🚀
#python #pytest #automation #apittesting #qa #allure #cicd #githubactions #testing #portfolio

