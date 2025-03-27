import requests
from api_framework.core.config import Config

class TransactionsClient:
    """
    API Client for interacting with the /transacoes resource.
    """
    def __init__(self, auth_headers: dict):
        """
        Initializes the TransactionsClient.

        Args:
            auth_headers (dict): A dictionary containing the authentication headers.
        """
        self.base_url = Config.APP_BASE_URL
        self.auth_headers = auth_headers

    def create_transaction(self, payload: dict) -> requests.Response:
        """
        Sends a POST request to create a new transaction.

        Args:
            payload (dict): The dictionary representing the transaction payload.

        Returns:
            requests.Response: The full response object from the API.
        """
        return requests.post(f"{self.base_url}/transacoes", json=payload, headers=self.auth_headers)

    def delete_transaction(self, transaction_id: int) -> requests.Response:
        """
        Sends a DELETE request to delete a transaction.

        Args:
            transaction_id (int): The ID of the transaction to delete.

        Returns:
            requests.Response: The full response object from the API.
        """
        return requests.delete(f"{self.base_url}/transacoes/{transaction_id}", headers=self.auth_headers)