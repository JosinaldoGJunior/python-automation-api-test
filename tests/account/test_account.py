import pytest
from assertpy import assert_that

from core.base_test import BaseTest


@pytest.mark.contas
class TestAccount(BaseTest):

    def test_should_create_account_successfully(self, headers, account_payload):

        response_create_account = self.post("contas", json=account_payload, headers=headers)
        self.check_status_code(response_create_account, 201)

        response_check_account = self.get("contas", headers=headers)
        self.check_status_code(response_check_account, 200)
        assert_that(response_check_account.json()).extracting("nome").contains(account_payload["nome"])

    def test_should_update_account(self, headers, account_payload, account_edit_payload):

        response_create_account = self.post("contas", json=account_payload, headers=headers)
        self.check_status_code(response_create_account, 201)
        account_id = response_create_account.json().get("id")

        response_edit_account = self.put(f"contas/{account_id}", json=account_edit_payload, headers=headers)
        self.check_status_code(response_edit_account, 200)

        response_get_account = self.get(f"contas/{account_id}", headers=headers)
        self.check_status_code(response_get_account, 200)
        assert_that(response_get_account.json().get("nome")).is_equal_to(account_edit_payload["nome"])


    def test_should_not_create_account_with_duplicate_name(self, headers, account_payload):

        response_create_account = self.post("contas",json=account_payload,headers=headers)
        self.check_status_code(response_create_account,201)

        response_create_same_account = self.post("contas",json=account_payload,headers=headers)
        self.check_status_code(response_create_same_account,400)
        assert_that(response_create_same_account.json()["error"]).is_equal_to("Já existe uma conta com esse nome!")


    def test_should_not_delete_a_account_with_transaction(self, headers, account_payload, transaction_payload):

        response_create_account = self.post("contas", json=account_payload, headers=headers)
        self.check_status_code(response_create_account, 201)
        account_id = response_create_account.json().get("id")
        transaction_payload["conta_id"] = account_id

        response_create_transaction = self.post("transacoes", json=transaction_payload, headers=headers)
        self.check_status_code(response_create_transaction, 201)

        response_delete_account = self.delete(f"contas/{account_id}",headers=headers)
        self.check_status_code(response_delete_account,500)
        assert_that(response_delete_account.json()["detail"]).contains("is still referenced from table")