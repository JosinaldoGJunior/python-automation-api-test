import requests
from assertpy import assert_that
import logging

from core.auth import Auth
from core.config import Config

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BaseTest:
    @property
    def base_url(self):
        return (
            f"{Config.APP_BASE_URL}{Config.APP_BASE_PATH}"
            if Config.APP_PORT == "443"
            else f"{Config.APP_BASE_URL}:{Config.APP_PORT}{Config.APP_BASE_PATH}"
        )

    def _build_url(self, endpoint):
        return f"{self.base_url}{endpoint}"

    def _build_headers(self, headers=None, include_auth=False):
        default_headers = {"Content-Type": Config.APP_CONTENT_TYPE}
        auth_headers = self.get_headers() if include_auth else {}
        return {**default_headers, **auth_headers, **(headers or {})}

    def get(self, endpoint, headers=None):
        url = self._build_url(endpoint)
        headers = self._build_headers(headers)
        logging.info(f"🔹 GET: {url}")
        return requests.get(url, headers=headers, timeout=Config.MAX_TIMEOUT)

    def post(self, endpoint, json=None, headers=None):
        url = self._build_url(endpoint)
        headers = self._build_headers(headers)
        logging.info(f"🔹 POST: {url} | Payload: {json}")
        return requests.post(url, json=json, headers=headers, timeout=Config.MAX_TIMEOUT)

    def put(self, endpoint, json=None, headers=None):
        url = self._build_url(endpoint)
        headers = self._build_headers(headers)
        logging.info(f"🔹 PUT: {url} | Payload: {json}")
        return requests.put(url, json=json, headers=headers, timeout=Config.MAX_TIMEOUT)

    def delete(self, endpoint, json=None, headers=None):
        url = self._build_url(endpoint)
        headers = self._build_headers(headers)
        logging.info(f"🔹 DELETE: {url} | Payload: {json}")
        return requests.delete(url, json=json, headers=headers, timeout=Config.MAX_TIMEOUT)

    @staticmethod
    def get_headers(self):
        return Auth.get_headers()

    @staticmethod
    def check_status_code(response, expected_status_code):
        logging.info(f"🔹 Complete response: {response.text}")
        logging.info("🔹 Expected Status Code: %s | Recebido: %s", expected_status_code, response.status_code)
        assert_that(response.status_code).is_equal_to(expected_status_code)
