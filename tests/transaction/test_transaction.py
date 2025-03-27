import pytest
from assertpy import assert_that

from core.base_test import BaseTest


@pytest.mark.transacao
class TestTransaction(BaseTest):


    def test_should_insert_transaction(self,headers,account_payload,transaction_payload):

        response_create_account = self.post("contas", json=account_payload, headers=headers)
        self.check_status_code(response_create_account, 201)
        account_id = response_create_account.json().get("id")
        transaction_payload["conta_id"] = account_id

        response_create_transaction = self.post("transacoes", json=transaction_payload, headers=headers)
        self.check_status_code(response_create_transaction, 201)

        response_get_transactions = self.get("transacoes", headers=headers)
        self.check_status_code(response_get_transactions, 200)
        assert_that(response_get_transactions.json()).extracting("descricao").contains(transaction_payload["descricao"])
        assert_that([float(item["valor"]) for item in response_get_transactions.json()]).contains(float(transaction_payload["valor"]))
        assert assert_that(response_get_transactions.json()).extracting("conta_id").contains(transaction_payload["conta_id"])



    def test_should_validate_required_fields(self,headers):

        response_create_transaction = self.post("transacoes", json={}, headers=headers)
        self.check_status_code(response_create_transaction, 400)

        expected_errors = [
            {"param": "data_transacao", "msg": "Data da Movimentação é obrigatório"},
            {"param": "data_pagamento", "msg": "Data do pagamento é obrigatório"},
            {"param": "descricao", "msg": "Descrição é obrigatório"},
            {"param": "envolvido", "msg": "Interessado é obrigatório"},
            {"param": "valor", "msg": "Valor é obrigatório"},
            {"param": "valor", "msg": "Valor deve ser um número"},
            {"param": "conta_id", "msg": "Conta é obrigatório"},
            {"param": "status", "msg": "Situação é obrigatório"},
        ]

        response_errors = response_create_transaction.json()
        missing_errors = [expected for expected in expected_errors if expected not in response_errors]
        assert not missing_errors, f"Mensagens ausentes: {missing_errors}"


    def test_should_reject_transaction_with_future_date(self, headers, future_transaction_payload):

        response_create_transaction = self.post("transacoes", json=future_transaction_payload, headers=headers)
        self.check_status_code(response_create_transaction,400)
        assert_that(response_create_transaction.json()).extracting("msg").contains("Data da Movimentação deve ser menor ou igual à data atual")

    def test_should_delete_a_transaction(self,headers,account_payload,transaction_payload):

        response_create_account = self.post("contas", json=account_payload, headers=headers)
        self.check_status_code(response_create_account, 201)
        account_id = response_create_account.json().get("id")
        transaction_payload["conta_id"] = account_id

        response_create_transaction = self.post("transacoes", json=transaction_payload, headers=headers)
        self.check_status_code(response_create_transaction, 201)

        transaction_id = response_create_transaction.json().get("id")
        response_delete_transaction = self.delete(f"transacoes/{transaction_id}",headers=headers)
        self.check_status_code(response_delete_transaction,204)