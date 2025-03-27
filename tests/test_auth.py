import pytest

@pytest.mark.auth
@pytest.mark.smoke
class TestAuth:


    def test_should_return_unauthorized_when_accessing_protected_endpoint(self, accounts_client):
        """
        Verifies that accessing a protected resource without an auth token
        is correctly rejected with a 401 Unauthorized status.
        """
        # Arrange
        # No specific data setup is needed.
        # The 'accounts_client' fixture is provided automatically by pytest.

        # Act
        # We use a dedicated method in the client that intentionally omits the auth token.
        response = accounts_client.get_accounts_without_auth()

        # Assert
        # We verify that the API correctly denies access.
        assert response.status_code == 401