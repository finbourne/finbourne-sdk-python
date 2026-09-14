# UpsertCurrencyGroupRequest

Request body for creating or updating a currency group.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the currency group. This uniquely identifies the currency group within the tenant. |
| **display_name** | **str** | Required | The name of the currency group. |
| **description** | **str** | Optional | A description for the currency group. |
| **major_unit_currency** | **str** | Required | The three-letter, case-sensitive currency code of the group&#39;s major unit, e.g. GBP for the sterling group. |
| **circulation_domain** | **str** | Optional | The domain in which the group&#39;s currencies circulate, e.g. an ISO 3166 country code. |
| **minor_units** | [List[CurrencyGroupMinorUnit]](CurrencyGroupMinorUnit.md) | Optional | The minor unit currencies belonging to this currency group. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertCurrencyGroupRequest import UpsertCurrencyGroupRequest

instance = UpsertCurrencyGroupRequest(
    code="...",  # required — The code of the currency group. This uniquely identifies the currency group within the tenant.
    display_name="...",  # required — The name of the currency group.
    description="...",  # optional — A description for the currency group.
    major_unit_currency="...",  # required — The three-letter, case-sensitive currency code of the group&#39;s major unit, e.g. GBP for the sterling group.
    circulation_domain="...",  # optional — The domain in which the group&#39;s currencies circulate, e.g. an ISO 3166 country code.
    minor_units=[]  # optional — The minor unit currencies belonging to this currency group.
)
```

- [CurrencyGroupMinorUnit](CurrencyGroupMinorUnit.md) — used in `minor_units`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

