import pytest
from assertpy import assert_that
from api_framework.utils import scenario_builder
from api_framework.utils import payload_generator


@pytest.mark.transactions
class TestTransaction:

    @pytest.mark.smoke
    @pytest.mark.positive
    def test_should_create_income_transaction_successfully(self, accounts_client, transactions_client):
        # Arrange - A precondition is that an account must exist.
        account_id = scenario_builder.create_account_and_get_id(accounts_client)
        payload = payload_generator.generate_new_income_payload(account_id)

        # Act - The main action under test is creating the transaction.
        response = transactions_client.create_transaction(payload)

        # Assert - We validate the response from the creation call itself.
        assert response.status_code == 201
        assert_that(response.json()['id']).is_not_none()
        assert_that(response.json()['descricao']).is_equal_to(payload['descricao'])
        assert_that(response.json()['tipo']).is_equal_to('REC')

    @pytest.mark.negative
    def test_should_validate_mandatory_fields_for_transaction(self, transactions_client):
        # Arrange - The scenario requires sending an empty payload.
        empty_payload = {}

        # Act - Attempt to create a transaction with the empty payload.
        response = transactions_client.create_transaction(empty_payload)

        # Assert - Validate the status code and the specific error messages.
        assert response.status_code == 400

        expected_errors = [
            "Data da Movimentação é obrigatório",
            "Data do pagamento é obrigatório",
            "Descrição é obrigatório",
            "Interessado é obrigatório",
            "Valor deve ser um número",
            "Valor é obrigatório",
            "Conta é obrigatório",
            "Situação é obrigatório"
        ]
        response_messages = [error['msg'] for error in response.json()]
        assert_that(response_messages).contains_only(*expected_errors)

    @pytest.mark.negative
    def test_should_not_create_transaction_with_future_date(self, accounts_client, transactions_client):
        # Arrange - Create a prerequisite account and a payload with a future date.
        account_id = scenario_builder.create_account_and_get_id(accounts_client)
        payload = payload_generator.generate_future_date_expense_payload(account_id)

        # Act - Attempt to create the transaction.
        response = transactions_client.create_transaction(payload)

        # Assert - Validate the specific business rule error.
        assert response.status_code == 400
        assert_that(response.json()[0]['msg']).is_equal_to("Data da Movimentação deve ser menor ou igual à data atual")

    @pytest.mark.positive
    def test_should_delete_transaction_successfully(self, accounts_client, transactions_client):
        # Arrange - We need an existing transaction to delete it.
        account_id = scenario_builder.create_account_and_get_id(accounts_client)
        transaction_id = scenario_builder.create_income_transaction_for_account(transactions_client, account_id)

        # Act - The action is to delete the transaction we just created.
        response = transactions_client.delete_transaction(transaction_id)

        # Assert - A successful deletion should return a 204 No Content status.
        assert response.status_code == 204