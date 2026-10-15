# PartnershipConfigPack

The partnership configuration pack a fund resolves to: the transaction types, chart of accounts and posting rules  the partners' ledger is booked under.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope of the configuration pack. |
| **code** | **str** | Required | The code of the configuration pack. |
| **version** | **str** | Required | The version of the configuration pack. |
| **transaction_types** | [List[PackTransactionType]](PackTransactionType.md) | Required | The partnership transaction types the pack provides. |
| **chart_of_accounts** | [List[PackAccount]](PackAccount.md) | Required | The accounts the pack posts partner capital to. |
| **posting_rules** | [List[PackPostingRule]](PackPostingRule.md) | Required | The rules that move each transaction type between its accounts. |
| **general_ledger_profile_code** | **str** | Optional | The code of the general ledger profile the pack&#39;s posting rules belong to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnershipConfigPack import PartnershipConfigPack

instance = PartnershipConfigPack(
    scope="...",  # required — The scope of the configuration pack.
    code="...",  # required — The code of the configuration pack.
    version="...",  # required — The version of the configuration pack.
    transaction_types=[],  # required — The partnership transaction types the pack provides.
    chart_of_accounts=[],  # required — The accounts the pack posts partner capital to.
    posting_rules=[],  # required — The rules that move each transaction type between its accounts.
    general_ledger_profile_code="..."  # optional — The code of the general ledger profile the pack&#39;s posting rules belong to.
)
```

- [PackTransactionType](PackTransactionType.md) — used in `transaction_types`
- [PackAccount](PackAccount.md) — used in `chart_of_accounts`
- [PackPostingRule](PackPostingRule.md) — used in `posting_rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

