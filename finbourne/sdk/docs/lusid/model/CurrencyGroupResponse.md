# CurrencyGroupResponse

A currency group: a set of related currencies sharing a major unit (e.g. GBP with minor unit GBX at 100:1).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional | The code of the currency group. This uniquely identifies the currency group within the tenant. |
| **display_name** | **str** | Optional | The name of the currency group. |
| **description** | **str** | Optional | A description for the currency group. |
| **major_unit_currency** | **str** | Optional | The three to five letter, case-sensitive currency code of the group&#39;s major unit, e.g. GBP for the sterling group. |
| **circulation_domain** | **str** | Optional | The domain in which the group&#39;s currencies circulate, e.g. an ISO 3166 country code. |
| **minor_units** | [List[CurrencyGroupMinorUnit]](CurrencyGroupMinorUnit.md) | Optional | The minor unit currencies belonging to this currency group. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CurrencyGroupResponse import CurrencyGroupResponse

instance = CurrencyGroupResponse(
    code="...",  # optional — The code of the currency group. This uniquely identifies the currency group within the tenant.
    display_name="...",  # optional — The name of the currency group.
    description="...",  # optional — A description for the currency group.
    major_unit_currency="...",  # optional — The three to five letter, case-sensitive currency code of the group&#39;s major unit, e.g. GBP for the sterling group.
    circulation_domain="...",  # optional — The domain in which the group&#39;s currencies circulate, e.g. an ISO 3166 country code.
    minor_units=[],  # optional — The minor unit currencies belonging to this currency group.
    version=Version(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource.
    links=[]  # optional
)
```

- [CurrencyGroupMinorUnit](CurrencyGroupMinorUnit.md) — used in `minor_units`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

