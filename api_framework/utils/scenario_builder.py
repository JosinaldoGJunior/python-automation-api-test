
from api_framework.clients.accounts_client import AccountsClient
from api_framework.clients.transactions_client import TransactionsClient
from api_framework.utils import payload_generator

def create_account_and_get_id(accounts_client, payload: dict = None) -> int:
    """
    Creates a valid account and returns its ID.

    If a payload is provided, it uses that payload.
    If no payload is provided, it generates a new one automatically.

    Args:
        accounts_client: An instance of AccountsClient.
        payload (dict, optional): A specific payload to use. Defaults to None.

    Returns:
        int: The ID of the newly created account.
    """
    if payload is None:
        payload = payload_generator.generate_account_payload()

    response = accounts_client.create_account(payload)
    response.raise_for_status()
    return response.json()['id']

def create_income_transaction_for_account(transactions_client: TransactionsClient, account_id: int) -> int:
    """
    Uses the TransactionsClient to create a valid income transaction
    for a specific account.

    Args:
        transactions_client: An instance of TransactionsClient.
        account_id: The ID of the account to which the transaction will be associated.

    Returns:
        int: The ID of the newly created transaction.
    """
    # 1. Generate a specific payload for an income transaction
    payload = payload_generator.generate_new_income_payload(account_id)

    # 2. Use the client to create the transaction via the API
    response = transactions_client.create_transaction(payload)

    # 3. Ensure the setup was successful
    response.raise_for_status()

    # 4. Extract and return the transaction ID
    return response.json()['id']