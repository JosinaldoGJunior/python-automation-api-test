from datetime import datetime, timedelta
import random
import uuid

now = datetime.now() - timedelta(days=1)
NOW_DATE = now.strftime("%d/%m/%Y")
FUTURE_DATE = (now + timedelta(days=5)).strftime("%d/%m/%Y")


def generate_account_payload():
   return {"nome": f"Conta{uuid.uuid4().hex[:5]}"}


def generate_account_edit_payload():
    return {"nome": f"E_Conta{uuid.uuid4().hex[:5]}"}


def generate_transaction_payload():
    return {
    "conta_id" : "",
    "descricao": f"Descricao_{uuid.uuid4().hex[:5]}",
    "envolvido" : f"Envolvidos_{uuid.uuid4().hex[:5]}",
    "tipo": random.choice(["DESP", "REC"]),
    "data_transacao" : NOW_DATE,
    "data_pagamento" : FUTURE_DATE,
    "valor" : round(random.uniform(500.00, 1000.00), 2),
    "status" : random.choice([True, False])
    }


def generate_future_transaction_payload():
    return {
    "conta_id" : "",
    "descricao": f"Descricao_{uuid.uuid4().hex[:5]}",
    "envolvido" : f"Envolvidos_{uuid.uuid4().hex[:5]}",
    "tipo": random.choice(["DESP", "REC"]),
    "data_transacao" : FUTURE_DATE,
    "data_pagamento" : FUTURE_DATE,
    "valor" : round(random.uniform(1.00, 1000.00), 2),
    "status" : random.choice([True, False])
    }

