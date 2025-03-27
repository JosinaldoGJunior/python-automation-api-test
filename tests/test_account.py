import pytest
from assertpy import assert_that

from api_framework.utils import scenario_builder


@pytest.mark.accounts
class TestAccount:

    @pytest.mark.smoke
    def test_should_create_account_successfully(self, accounts_client, account_payload):
        # Arrange - The necessary data is injected by the 'account_payload' fixture.

        # Act - The primary action to be tested is performed using the client.
        response = accounts_client.create_account(account_payload)

        # Assert - The response from the action is thoroughly validated.
        assert response.status_code == 201
        assert_that(response.json()['nome']).is_equal_to(account_payload['nome'])
        assert_that(response.json()['id']).is_not_none()

    @pytest.mark.negative
    def test_should_not_create_account_with_duplicate_name(self, accounts_client, account_payload):
        # Arrange - Create an initial account to set up the "duplicate" precondition.
        scenario_builder.create_account_and_get_id(accounts_client,account_payload)

        # Act - Attempt to create the exact same account a second time.
        response = accounts_client.create_account(account_payload)

        # Assert - Validate the specific duplication error message.
        assert response.status_code == 400
        assert_that(response.json()['error']).is_equal_to("Já existe uma conta com esse nome!")

    @pytest.mark.regression
    def test_should_update_account_successfully(self, accounts_client, account_edit_payload):
        # Arrange - Create an account to have a resource to update.
        account_id = scenario_builder.create_account_and_get_id(accounts_client)

        # Act - Perform the update action on the newly created account.
        response = accounts_client.update_account(account_id, account_edit_payload)

        # Assert - Validate that the UPDATE action was successful and the data was changed.
        assert response.status_code == 200
        assert_that(response.json()['nome']).is_equal_to(account_edit_payload['nome'])

    @pytest.mark.negative
    def test_should_not_delete_account_with_transactions(self, accounts_client, transactions_client):
        # Arrange - A complex scenario is built cleanly.
        # 1. We need an account.
        account_id = scenario_builder.create_account_and_get_id(accounts_client)
        # 2. We need a transaction linked to that account.
        scenario_builder.create_income_transaction_for_account(transactions_client, account_id)

        # Act - Attempt to delete the parent account.
        response = accounts_client.delete_account(account_id)

        # Assert - Validate that the API returns a server error due to the database constraint.
        assert response.status_code == 500
        assert "is still referenced from table" in response.json()['detail']