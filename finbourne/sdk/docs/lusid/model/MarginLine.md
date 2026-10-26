# MarginLine

One holding's contribution to a margin call: its exposure, or its value as collateral.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **str** | Required | The run that produced the line. |
| **agreement_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **item** | **str** | Required | The margin item the line falls under. Filterable. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **holding_id** | **str** | Optional | The holding the line was valued from. |
| **custodian_account_scope** | **str** | Optional | The scope of the custodian account the holding sits in, when it has one. |
| **custodian_account_code** | **str** | Optional | The code of the custodian account the holding sits in, when it has one. |
| **custodian_account_name** | **str** | Optional | The name of the custodian account, when it has one. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The identifiers of the instrument held. |
| **units** | **float** | Required | The units held. |
| **pv** | **float** | Optional | The present value of the holding in the agreement&#39;s base currency, when it contributes to exposure. |
| **variation_margin** | **float** | Optional | The holding&#39;s contribution to variation margin, when it contributes to exposure. |
| **collateral_value** | **float** | Optional | The holding&#39;s value as collateral after haircuts, when it is held as collateral. |
| **initial_margin_item** | **str** | Optional | The initial-margin item the line falls under, when the holding matched one. Filterable. |
| **initial_margin** | **float** | Optional | The holding&#39;s share of its netting set&#39;s initial margin, before the threshold, when it contributes to it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginLine import MarginLine

instance = MarginLine(
    run_id="...",  # required — The run that produced the line.
    agreement_id=ResourceId(...),  # required
    item="...",  # required — The margin item the line falls under. Filterable.
    portfolio_id=ResourceId(...),  # optional
    holding_id="...",  # optional — The holding the line was valued from.
    custodian_account_scope="...",  # optional — The scope of the custodian account the holding sits in, when it has one.
    custodian_account_code="...",  # optional — The code of the custodian account the holding sits in, when it has one.
    custodian_account_name="...",  # optional — The name of the custodian account, when it has one.
    instrument_identifiers=,  # required — The identifiers of the instrument held.
    units=0.0,  # required — The units held.
    pv=0.0,  # optional — The present value of the holding in the agreement&#39;s base currency, when it contributes to exposure.
    variation_margin=0.0,  # optional — The holding&#39;s contribution to variation margin, when it contributes to exposure.
    collateral_value=0.0,  # optional — The holding&#39;s value as collateral after haircuts, when it is held as collateral.
    initial_margin_item="...",  # optional — The initial-margin item the line falls under, when the holding matched one. Filterable.
    initial_margin=0.0  # optional — The holding&#39;s share of its netting set&#39;s initial margin, before the threshold, when it contributes to it.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

