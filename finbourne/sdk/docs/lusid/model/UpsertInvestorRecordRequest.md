# UpsertInvestorRecordRequest

Request to create or update an investor record
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope in which the Investor Record lies. |
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Required | Unique client-defined identifiers of the Investor Record. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties associated to the Investor Record. |
| **display_name** | **str** | Required | The display name of the Investor Record |
| **description** | **str** | Optional | The description of the Investor Record |
| **investor** | [InvestorIdentifier](InvestorIdentifier.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInvestorRecordRequest import UpsertInvestorRecordRequest

instance = UpsertInvestorRecordRequest(
    scope="...",  # required — The scope in which the Investor Record lies.
    identifiers=ModelProperty(...),  # required — Unique client-defined identifiers of the Investor Record.
    properties=ModelProperty(...),  # optional — A set of properties associated to the Investor Record.
    display_name="...",  # required — The display name of the Investor Record
    description="...",  # optional — The description of the Investor Record
    investor=InvestorIdentifier(...)  # required
)
```

- [ModelProperty](ModelProperty.md) — used in `identifiers`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [InvestorIdentifier](InvestorIdentifier.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

