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
| **scenario** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **line_key** | **str** | Optional | A key that identifies the line within its run, with which its explanation is asked for. A line valued under a scenario has a different key from the same holding in the base market. Null for a line stored before lines carried a key. |
| **explain_available** | **bool** | Optional | Whether the working behind the line&#39;s figures was stored, so that the line can be explained. One flag covers every figure of the line. |
| **instrument_type** | **str** | Optional | LUSID&#39;s type for the instrument held, when the run read it. |
| **asset_class** | **str** | Optional | The instrument&#39;s asset class, when the run read it. |
| **currency** | **str** | Optional | The currency the holding is denominated in, when the run read it. |
| **maturity_date** | **datetime** | Optional | The instrument&#39;s maturity, when it has one. |
| **notional** | **float** | Optional | The holding&#39;s notional in its own currency, when the instrument has one. |
| **gross_initial_margin** | **float** | Optional | The regulatory-grid charge on the holding before its netting set&#39;s net-to-gross scaling. Null under other methods. |
| **movable_to** | **List[str]** | Required | The initial-margin netting sets of other agreements in the run the holding could be re-booked into, as scope/code/item. Recorded for base-case trading lines under an initial-margin item; empty otherwise. |


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
    initial_margin=0.0,  # optional — The holding&#39;s share of its netting set&#39;s initial margin, before the threshold, when it contributes to it.
    scenario=ResourceId(...),  # optional
    line_key="...",  # optional — A key that identifies the line within its run, with which its explanation is asked for. A line valued under a scenario has a different key from the same holding in the base market. Null for a line stored before lines carried a key.
    explain_available=True,  # optional — Whether the working behind the line&#39;s figures was stored, so that the line can be explained. One flag covers every figure of the line.
    instrument_type="...",  # optional — LUSID&#39;s type for the instrument held, when the run read it.
    asset_class="...",  # optional — The instrument&#39;s asset class, when the run read it.
    currency="...",  # optional — The currency the holding is denominated in, when the run read it.
    maturity_date=datetime.now(),  # optional — The instrument&#39;s maturity, when it has one.
    notional=0.0,  # optional — The holding&#39;s notional in its own currency, when the instrument has one.
    gross_initial_margin=0.0,  # optional — The regulatory-grid charge on the holding before its netting set&#39;s net-to-gross scaling. Null under other methods.
    movable_to=  # required — The initial-margin netting sets of other agreements in the run the holding could be re-booked into, as scope/code/item. Recorded for base-case trading lines under an initial-margin item; empty otherwise.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

