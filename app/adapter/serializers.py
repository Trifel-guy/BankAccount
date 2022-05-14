def single_customer_serializer(user) -> dict:
    return {
        "id": str(user["id"]),
        "lastname": user["lastname"],
        "firstname": user["firstname"],
    }

def customers_serializer(users) -> list:
    return [single_customer_serializer(user) for user in users]


def single_account_serializer(account) -> dict:
    return {
        "id": str(account["id"]),
        "balance": account["balance"],
        "created_at": account["created_at"],
        "account_owner": account["account_owner"],
        "list_operation": account["list_operation"] if "list_operation" in account else [],
    }

def accounts_serializer(accounts) -> list:
    return [single_account_serializer(account) for account in accounts]

def single_operation_serializer(operation) -> dict:
    return {
        "id": str(operation["id"]),
        "balance": operation["balance"],
        "created_at": operation["created_at"],
        "account_owner": operation["account_owner"],
    }

def operations_serializer(operations) -> list:
    return [single_operation_serializer(operation) for operation in operations]