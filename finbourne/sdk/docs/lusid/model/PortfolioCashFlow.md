# PortfolioCashFlow

The details for the cashflow for a given portfolio.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_by_id** | **int** | Required | The groupBy subHoldings and currency. |
| **sequence_number** | **int** | Required | Sequence number determining the order of the cash flow records. |
| **effective_date** | **datetime** | Optional | Indicates the date when the cash-flow settles. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. |
| **type** | **str** | Required | Indicates the record type (Closed, Open, Activity). |
| **movement_name** | **str** | Required | Indicates the specific movement of the transaction that generated this cash flow. |
| **cashflow** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **balance** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **fx_rate** | **float** | Required | Exchange rate between the currency of this cash flow and the reporting currency. |
| **cashflow_reporting_currency** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **balance_reporting_currency** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **translation_gain_loss** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **cost_basis_reporting_currency** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **transaction** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **unrealised_gain_loss_reporting_currency** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioCashFlow import PortfolioCashFlow

instance = PortfolioCashFlow(
    group_by_id=0,  # required — The groupBy subHoldings and currency.
    sequence_number=0,  # required — Sequence number determining the order of the cash flow records.
    effective_date=datetime.now(),  # optional — Indicates the date when the cash-flow settles.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio.
    type="...",  # required — Indicates the record type (Closed, Open, Activity).
    movement_name="...",  # required — Indicates the specific movement of the transaction that generated this cash flow.
    cashflow=CurrencyAndAmount(...),  # required
    balance=CurrencyAndAmount(...),  # required
    fx_rate=0.0,  # required — Exchange rate between the currency of this cash flow and the reporting currency.
    cashflow_reporting_currency=CurrencyAndAmount(...),  # required
    balance_reporting_currency=CurrencyAndAmount(...),  # required
    translation_gain_loss=CurrencyAndAmount(...),  # required
    cost_basis_reporting_currency=CurrencyAndAmount(...),  # required
    transaction=Transaction(...),  # optional
    unrealised_gain_loss_reporting_currency=CurrencyAndAmount(...),  # required
    links=[]  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [Transaction](Transaction.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

