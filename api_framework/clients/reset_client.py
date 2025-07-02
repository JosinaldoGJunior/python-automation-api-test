
import requests
from api_framework.core.config import Config # Importa a classe Config

class ResetClient:
    """
    API Client for interacting with the /reset resource.
    """
    def __init__(self, auth_headers: dict):
        """
        Initializes the ResetClient.

        Args:
            auth_headers (dict): A dictionary containing the authentication headers.
        """
        self.base_url = Config.APP_BASE_URL
        self.auth_headers = auth_headers

    def reset_state_with_auth(self) -> requests.Response:
        """
        Sends an authenticated GET request to /reset to clear user data.
        """
        return requests.get(f"{self.base_url}/reset", headers=self.auth_headers)

    def reset_state_without_auth(self) -> requests.Response:
        """
        Sends a non-authenticated GET request to /reset.
        """
        return requests.get(f"{self.base_url}/reset")