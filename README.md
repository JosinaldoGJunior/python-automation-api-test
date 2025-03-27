# Finance API Tests

This project was developed to showcase my skills in API test automation, using modern tools and best practices. The implementation focuses on scalability, clarity, and efficiency, making it ideal for real financial control scenarios.

## ⚡ Technologies Used
- **Python** — Main language for automation.  
- **Pytest** — Robust framework for test creation and execution.  
- **Allure Reports** — Interactive and detailed report generation.  
- **GitHub Actions** — Continuous Integration (CI/CD) for automated builds and test execution.  
- **Requests** — Library for efficient HTTP requests.  
- **AssertPy** — Framework for clearer and more precise assertions.  
- **Pydantic** — For data validation and manipulation in payloads.

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

## ✅ Key Features and Best Practices
- **Modular organization** — Clean and organized structure for scalability and maintenance.  
- **`.env` Configuration** — Secure storage for tokens, URLs, and other credentials.  
- **Comprehensive Testing** — Coverage for both positive and negative scenarios:  
  - Account creation, editing, and deletion.  
  - Transaction validation and positive/negative balance checks.  
  - Negative tests for critical scenarios and invalid inputs.  
- **Allure Reports** — Detailed results and visual charts for better analysis.  
- **CI/CD Pipeline with GitHub Actions** — Full automation to ensure continuous project validation.

## ⚙️ Installation and Execution
### 1. **Clone the Repository**
```
git clone https://github.com/your-username/finance-api-tests.git
cd finance-api-tests
```

### 2. **Install Dependencies**
```
pip install -r requirements.txt
```

### 3. **Set Environment Variables**
Create a `.env` file in the project's root and add your credentials:
```
API_URL=https://example.com/api
TOKEN=your_token_here
```

### 4. **Run Tests**
- To run all tests with Allure report:
```
pytest --alluredir=allure-results
allure serve allure-results
```

- To run a specific test suite (e.g., transactions):
```
pytest tests/transaction
```

### 5. **Execution via CI/CD**
The **GitHub Actions** pipeline is automatically triggered on each `push` or `pull request`, ensuring continuous project validation.

## 🔍 Allure Report Example
The Allure report includes:  
✅ Interactive execution charts  
✅ Detailed logs for precise analysis  
✅ Automatic screenshot capture in case of failures  

## ⭐ Project Highlights
✅ Organized and modular structure.  
✅ Detailed and visual reports with Allure.  
✅ Automated CI/CD pipeline via GitHub Actions.  
✅ Secure use of tokens and environment variables.  
✅ Comprehensive coverage of critical scenarios and negative tests.  

---

For further details or collaboration, feel free to reach out. 🚀
#python #pytest #automation #apittesting #qa #allure #cicd #githubactions #testing #portfolio

