# AccountHolder

An Account Holder of an Investment Account.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Optional | A client-defined key used to identify the Account Holder, unique within the Investment Account |
| **scope** | **str** | Optional | The scope in which the Investor Record lies. |
| **identifiers** | **Dict[str, Optional[str]]** | Optional | Single Account Holder identifier that should target the desired Investor Record. |
| **entity_unique_id** | **str** | Optional | The unique InvestorRecord entity identifier |
| **investor_record** | [InvestorRecord](InvestorRecord.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccountHolder import AccountHolder

instance = AccountHolder(
    key="...",  # optional — A client-defined key used to identify the Account Holder, unique within the Investment Account
    scope="...",  # optional — The scope in which the Investor Record lies.
    identifiers=,  # optional — Single Account Holder identifier that should target the desired Investor Record.
    entity_unique_id="...",  # optional — The unique InvestorRecord entity identifier
    investor_record=InvestorRecord(...)  # optional
)
```

- [InvestorRecord](InvestorRecord.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

