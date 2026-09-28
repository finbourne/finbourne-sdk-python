# ComplianceRuleContribution

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **index** | **int** | Required | The position of this contribution within the compliance run. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **order_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument** | **str** | Required | The LUSID instrument identifier (LUID) of the instrument for this contribution. |
| **instrument_type** | **str** | Optional | Optional. The economic type of the instrument for this contribution. |
| **holding_type** | **str** | Optional | Optional. The holding type of this contribution. |
| **holding_id** | **str** | Optional | Optional. The internal holding identifier encoding the detail of what the holding includes. |
| **result_values** | **Dict[str, float]** | Required | Dictionary of AddressKey (as string) and their corresponding decimal valuation results for this contribution. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Required | Dictionary of PropertyKey (as string) and their corresponding property for this contribution. |
| **related_properties** | **Dict[str, Optional[str]]** | Required | Dictionary of related property keys (as string) and their string values, read from related entities across a relationship. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleContribution import ComplianceRuleContribution

instance = ComplianceRuleContribution(
    index=0,  # required — The position of this contribution within the compliance run.
    portfolio_id=ResourceId(...),  # required
    order_id=ResourceId(...),  # optional
    instrument="...",  # required — The LUSID instrument identifier (LUID) of the instrument for this contribution.
    instrument_type="...",  # optional — Optional. The economic type of the instrument for this contribution.
    holding_type="...",  # optional — Optional. The holding type of this contribution.
    holding_id="...",  # optional — Optional. The internal holding identifier encoding the detail of what the holding includes.
    result_values=,  # required — Dictionary of AddressKey (as string) and their corresponding decimal valuation results for this contribution.
    properties=ModelProperty(...),  # required — Dictionary of PropertyKey (as string) and their corresponding property for this contribution.
    related_properties=  # required — Dictionary of related property keys (as string) and their string values, read from related entities across a relationship.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

