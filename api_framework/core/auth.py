import requests
import logging
import os
from datetime import datetime, timedelta
from typing import Optional, Dict

class Auth:
    """
    Manages API authentication, providing a cached token with expiry.
    This class uses a Singleton pattern approach with class-level variables.
    """
    _token: Optional[str] = None
    _token_expiry: Optional[datetime] = None

    @staticmethod
    def get_token() -> str:
        """
        Retrieves an authentication token.

        It returns a cached token if it's still valid, otherwise, it requests a new one.

        Raises:
            RuntimeError: If authentication fails for any reason.

        Returns:
            str: The JWT authentication token.
        """
        # Return cached token if it exists and has not expired
        if Auth._token and Auth._token_expiry and datetime.now() < Auth._token_expiry:
            return Auth._token

        logging.info("Token is expired or not present, generating a new one...")
        login_url = os.getenv("API_LOGIN_URL") # Assumes BASE_URL is for the main app, not auth
        login_payload = {
            "email": os.getenv("API_EMAIL"),
            "senha": os.getenv("API_PASSWORD")
        }

        if not all([login_url, login_payload["email"], login_payload["senha"]]):
            raise ValueError("API credentials and login URL must be set in environment variables.")

        try:
            response = requests.post(login_url, json=login_payload, timeout=10)
            response.raise_for_status()  # Fails for 4xx or 5xx status codes
        except requests.RequestException as e:
            raise RuntimeError(f"Authentication request failed: {e}") from e

        token_data = response.json()
        Auth._token = token_data.get("token")
        Auth._token_expiry = datetime.now() + timedelta(minutes=30)

        if not Auth._token:
            raise RuntimeError(f"Authentication succeeded but no token was found in response: {response.text}")

        logging.info("🔹 Token generated successfully.")
        return Auth._token

    @staticmethod
    def get_headers(extra_headers: Optional[Dict] = None) -> Dict[str, str]:
        """
        Builds the standard authentication headers.

        Args:
            extra_headers (dict, optional): Any extra headers to merge. Defaults to None.

        Returns:
            dict: A dictionary of headers including the Authorization token.
        """
        headers = {"Authorization": f"JWT {Auth.get_token()}"}
        if extra_headers:
            headers.update(extra_headers)
        return headers