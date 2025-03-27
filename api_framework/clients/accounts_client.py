import requests
from api_framework.core.config import Config

class AccountsClient:
    """
    API Client for interacting with the /contas resource.
    """
    def __init__(self, auth_headers: dict):
        """
        Initializes the AccountsClient.

        Args:
            auth_headers (dict): A dictionary containing the authentication headers (e.g., {"Authorization": "JWT ..."}).
        """
        self.base_url = Config.APP_BASE_URL
        self.auth_headers = auth_headers

    def create_account(self, payload: dict) -> requests.Response:
        """
        Sends a POST request to create a new account.

        Args:
            payload (dict): The dictionary representing the account payload.

        Returns:
            requests.Response: The full response object from the API.
        """
        return requests.post(f"{self.base_url}/contas", json=payload, headers=self.auth_headers)

    def update_account(self, account_id: int, payload: dict) -> requests.Response:
        """
        Sends a PUT request to update an existing account.

        Args:
            account_id (int): The ID of the account to update.
            payload (dict): The dictionary representing the new account data.

        Returns:
            requests.Response: The full response object from the API.
        """
        return requests.put(f"{self.base_url}/contas/{account_id}", json=payload, headers=self.auth_headers)

    def delete_account(self, account_id: int) -> requests.Response:
        """
        Sends a DELETE request to delete an account.

        Args:
            account_id (int): The ID of the account to delete.

        Returns:
            requests.Response: The full response object from the API.
        """
        return requests.delete(f"{self.base_url}/contas/{account_id}", headers=self.auth_headers)

    def get_accounts_without_auth(self) -> requests.Response:
        """
        Sends a non-authenticated GET request to /contas.
        Intended for use in authentication tests.

        Returns:
            requests.Response: The full response object from the API.
        """
        return requests.get(f"{self.base_url}/contas")