import pytest
from dotenv import load_dotenv

from core.base_test import Auth
from core.payload import generate_account_payload, generate_account_edit_payload, generate_transaction_payload, generate_future_transaction_payload
import shutil
import os

load_dotenv()

@pytest.fixture(scope='session', autouse=True)
def load_env_variables():
    os.environ["BASE_URL"] = os.getenv("BASE_URL")
    os.environ["API_LOGIN_URL"] = os.getenv("API_LOGIN_URL")
    os.environ["API_EMAIL"] = os.getenv("API_EMAIL")
    os.environ["API_PASSWORD"] = os.getenv("API_PASSWORD")

@pytest.fixture(scope="session")
def headers():
    headers =  Auth.get_headers()
    return headers


def pytest_sessionfinish(session, exitstatus):
    """Hook to check if allure-results contains data after testing."""
    results_dir = "allure-results"
    if not os.listdir(results_dir):
        print("⚠️ Error: No results were generated in the allure-results directory.")


@pytest.fixture
def account_payload():
    return generate_account_payload()

@pytest.fixture
def account_edit_payload():
    return generate_account_edit_payload()

@pytest.fixture
def transaction_payload():
    return (generate_transaction_payload())

@pytest.fixture
def future_transaction_payload():
    return generate_future_transaction_payload()


def pytest_sessionstart(session):
    """Hook to clear the allure-results folder before starting the tests."""
    results_dir = "allure-results"
    if os.path.exists(results_dir):
        def onerror(func, path, exc_info):
            os.chmod(path, 0o777)
            func(path)

        shutil.rmtree(results_dir, onerror=onerror)

    os.makedirs(results_dir)