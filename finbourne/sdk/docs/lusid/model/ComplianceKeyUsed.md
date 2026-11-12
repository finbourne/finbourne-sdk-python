# ComplianceKeyUsed

A key a holding contributed to the rule: the key, the role(s) it played in the rule, the holding's own value for  it, and which bag the value was read from.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | *No description available.* |
| **roles** | **List[str]** | Required | *No description available.* |
| **value** | **object** | Optional | This holding&#39;s own value for the key. Polymorphic: a number for a result or metric property, a label string for  a label property, or a string for a related property. |
| **source** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceKeyUsed import ComplianceKeyUsed

instance = ComplianceKeyUsed(
    key="...",  # required
    roles=,  # required
    value=,  # optional — This holding&#39;s own value for the key. Polymorphic: a number for a result or metric property, a label string for  a label property, or a string for a related property.
    source="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

