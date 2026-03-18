# GeneralLedgerProfileResponse

A General Ledger Profile Definition.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **chart_of_accounts_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **general_ledger_profile_code** | **str** | Required | The unique code for the General Ledger Profile |
| **display_name** | **str** | Required | The name of the General Ledger Profile |
| **description** | **str** | Optional | A description for the General Ledger Profile |
| **general_ledger_profile_mappings** | [List[GeneralLedgerProfileMapping]](GeneralLedgerProfileMapping.md) | Required | Rules for mapping Account or property values to aggregation pattern definitions |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GeneralLedgerProfileResponse import GeneralLedgerProfileResponse

instance = GeneralLedgerProfileResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    chart_of_accounts_id=ResourceId(...),  # required
    general_ledger_profile_code="...",  # required — The unique code for the General Ledger Profile
    display_name="...",  # required — The name of the General Ledger Profile
    description="...",  # optional — A description for the General Ledger Profile
    general_ledger_profile_mappings=[],  # required — Rules for mapping Account or property values to aggregation pattern definitions
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [GeneralLedgerProfileMapping](GeneralLedgerProfileMapping.md) — used in `general_ledger_profile_mappings`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

