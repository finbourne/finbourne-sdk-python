# GeneralLedgerProfileRequest

A General Ledger Profile Definition.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **general_ledger_profile_code** | **str** | Required | The unique code for the General Ledger Profile |
| **display_name** | **str** | Required | The name of the General Ledger Profile |
| **description** | **str** | Optional | A description for the General Ledger Profile |
| **general_ledger_profile_mappings** | [List[GeneralLedgerProfileMapping]](GeneralLedgerProfileMapping.md) | Required | Rules for mapping Account or property values to aggregation pattern definitions |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GeneralLedgerProfileRequest import GeneralLedgerProfileRequest

instance = GeneralLedgerProfileRequest(
    general_ledger_profile_code="...",  # required — The unique code for the General Ledger Profile
    display_name="...",  # required — The name of the General Ledger Profile
    description="...",  # optional — A description for the General Ledger Profile
    general_ledger_profile_mappings=[]  # required — Rules for mapping Account or property values to aggregation pattern definitions
)
```

- [GeneralLedgerProfileMapping](GeneralLedgerProfileMapping.md) — used in `general_ledger_profile_mappings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

