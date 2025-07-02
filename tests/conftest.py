import pytest
import os
import shutil
from dotenv import load_dotenv

from api_framework.core.auth import Auth
from api_framework.clients.accounts_client import AccountsClient
from api_framework.clients.transactions_client import TransactionsClient
from api_framework.clients.reset_client import ResetClient
from api_framework.utils import payload_generator

load_dotenv()


# --- HOOKS for setup and teardown ---

def pytest_sessionstart(session):
    """
    Hook to clear the allure-results folder before starting the test session.
    """
    results_dir = "allure-results"
    if os.path.exists(results_dir):
        def onerror(func, path, exc_info):
            os.chmod(path, 0o777)
            func(path)
        shutil.rmtree(results_dir, onerror=onerror)
    os.makedirs(results_dir)


def pytest_sessionfinish(session, exitstatus):
    """
    Hook to check if allure-results contains data after the test session.
    """
    results_dir = "allure-results"
    if not os.path.isdir(results_dir) or not os.listdir(results_dir):
        print("\n⚠️ Warning: No results were generated in the allure-results directory.")


# --- FIXTURES for Authentication and API Clients ---

@pytest.fixture(scope="session")
def auth_headers() -> dict:
    """
    Session-scoped fixture to perform login only once and provide auth headers.
    """
    return Auth.get_headers()


@pytest.fixture(scope="session")
def accounts_client(auth_headers: dict) -> AccountsClient:
    """
    Session-scoped fixture that provides an initialized AccountsClient.
    """
    return AccountsClient(auth_headers=auth_headers)


@pytest.fixture(scope="session")
def transactions_client(auth_headers: dict) -> TransactionsClient:
    """
    Session-scoped fixture that provides an initialized TransactionsClient.
    """
    return TransactionsClient(auth_headers=auth_headers)


@pytest.fixture(scope="session")
def reset_client(auth_headers: dict) -> ResetClient:
    """
    Session-scoped fixture that provides an initialized ResetClient.
    """
    return ResetClient(auth_headers=auth_headers)



@pytest.fixture
def account_payload() -> dict:
    """
    Function-scoped fixture to provide a new, random account payload for each test.
    """
    return payload_generator.generate_account_payload()


@pytest.fixture
def account_edit_payload() -> dict:
    """
    Provides a new payload for editing an account.
    """
    return payload_generator.generate_account_edit_payload()


@pytest.fixture
def income_transaction_payload() -> dict:
    """
    Provides a new payload for an INCOME transaction. This is now deterministic.
    """
    return payload_generator.generate_new_income_payload(account_id=None)


@pytest.fixture
def expense_transaction_payload() -> dict:
    """
    Provides a new payload for an EXPENSE transaction. This is deterministic.
    """
    return payload_generator.generate_new_expense_payload(account_id=None)


@pytest.fixture(scope="session", autouse=True)
def clean_environment_before_run(auth_headers):
    """
    Runs automatically at the start of the session to ensure a clean state
    by calling the /reset endpoint.
    It depends on auth_headers to ensure login happens first.
    """
    from api_framework.clients.reset_client import ResetClient

    print("\nResetting application state before test run...")
    reset_client = ResetClient(auth_headers=auth_headers)
    response = reset_client.reset_state_with_auth()

    response.raise_for_status()
    print("State reset successfully.")

    import os
    from dotenv import load_dotenv

    load_dotenv()

    class Config:
        @staticmethod
        def get_base_url():
            return os.getenv("BASE_URL")