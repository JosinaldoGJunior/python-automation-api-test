import random
from datetime import datetime, timedelta
import uuid


def _random_string(length: int) -> str:
    """Generates a random alphanumeric string of a given length."""
    return uuid.uuid4().hex[:length]

def _random_value(min_val: float, max_val: float) -> float:
    """Generates a random float value within a given range."""
    val = random.uniform(min_val, max_val)
    return round(val, 2)

def _get_date_as_string(days_offset: int = 0) -> str:
    """
    Gets a date as a string in 'DD/MM/YYYY' format, which the target API expects.
    """
    date = datetime.now() + timedelta(days=days_offset)
    return date.strftime('%d/%m/%Y') # Formato correto para a API



def generate_account_payload() -> dict:
    """Generates a payload for a new account."""
    return {"nome": f"Account_{_random_string(8)}"}

def generate_account_edit_payload() -> dict:
    """Generates a payload for editing an account."""
    return {"nome": f"Account_Edited_{_random_string(5)}"}

def generate_new_income_payload(account_id: int) -> dict:
    """

    Generates a deterministic payload for a new INCOME ("RECEITA") transaction.
    """
    return {
        "conta_id": account_id,
        "descricao": f"Income transaction {_random_string(5)}",
        "envolvido": "Company Inc.",
        "tipo": "REC",
        "data_transacao": _get_date_as_string(-1), # Ontem
        "data_pagamento": _get_date_as_string(5),
        "valor": _random_value(100.0, 1500.0),
        "status": True
    }

def generate_new_expense_payload(account_id: int, paid_status: bool = False) -> dict:
    """
    Generates a deterministic payload for a new EXPENSE ("DESPESA") transaction.
    """
    return {
        "conta_id": account_id,
        "descricao": f"Expense transaction {_random_string(5)}",
        "envolvido": "Supermarket",
        "tipo": "DESP",
        "data_transacao": _get_date_as_string(-2), # Anteontem
        "data_pagamento": _get_date_as_string(10),
        "valor": _random_value(50.0, 500.0),
        "status": paid_status
    }

def generate_future_date_expense_payload(account_id: int) -> dict:
    """
    Generates a payload for an EXPENSE transaction with a future date.
    """
    return {
        "conta_id": account_id,
        "descricao": f"Future expense {_random_string(5)}",
        "envolvido": "Online Store",
        "tipo": "DESP",
        "data_transacao": _get_date_as_string(5),
        "data_pagamento": _get_date_as_string(10),
        "valor": _random_value(10.0, 100.0),
        "status": False
    }