import pytest

@pytest.mark.auth
@pytest.mark.smoke
class TestAuth:


    def test_should_return_unauthorized_when_accessing_protected_endpoint(self, accounts_client):
        # Act
        response = accounts_client.get_accounts_without_auth()

        # Assert
        assert response.status_code == 401