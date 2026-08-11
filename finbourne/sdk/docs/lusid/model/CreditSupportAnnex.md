# CreditSupportAnnex

Entity to capture the calculable and queryable methods and practices of determining and transferring collateral  to a counterparty as part of margining of transactions. These typically come from a particular ISDA agreement  that is in place between the two counterparties.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reference_currency** | **str** | Required | The base, or reference, currency against which MtM value and exposure should be calculated  and in which the CSA parameters are defined if the currency is not otherwise explicitly stated. |
| **collateral_currencies** | **List[str]** | Required | The set of currencies within which it is acceptable to post cash collateral. |
| **isda_agreement_version** | **str** | Required | The transactions will take place with reference to a particular ISDA master agreement. This  will likely be either the ISDA 1992 or ISDA 2002 agremeents or ISDA close-out 2009. |
| **margin_call_frequency** | **str** | Required | The tenor, e.g. daily (1D) or biweekly (2W), at which frequency a margin call will be made, calculations  made and money transferred to readjust. The calculation might also require a specific time for valuation and notification. |
| **valuation_agent** | **str** | Required | Are the calculations performed by the institutions&#39;s counterparty or the institution trading with them. |
| **threshold_amount** | **float** | Required | At what level of exposure does collateral need to be posted. Will typically be zero for banks.  Should be stated in reference currency |
| **rounding_decimal_places** | **int** | Required | Where a calculation needs to be rounded to a specific number of decimal places,  this states the number that that requires. |
| **initial_margin_amount** | **float** | Required | The initial margin that is required. In the reference currency |
| **minimum_transfer_amount** | **float** | Required | The minimum amount, in the reference currency, that must be transferred when required. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreditSupportAnnex import CreditSupportAnnex

instance = CreditSupportAnnex(
    reference_currency="...",  # required — The base, or reference, currency against which MtM value and exposure should be calculated  and in which the CSA parameters are defined if the currency is not otherwise explicitly stated.
    collateral_currencies=,  # required — The set of currencies within which it is acceptable to post cash collateral.
    isda_agreement_version="...",  # required — The transactions will take place with reference to a particular ISDA master agreement. This  will likely be either the ISDA 1992 or ISDA 2002 agremeents or ISDA close-out 2009.
    margin_call_frequency="...",  # required — The tenor, e.g. daily (1D) or biweekly (2W), at which frequency a margin call will be made, calculations  made and money transferred to readjust. The calculation might also require a specific time for valuation and notification.
    valuation_agent="...",  # required — Are the calculations performed by the institutions&#39;s counterparty or the institution trading with them.
    threshold_amount=0.0,  # required — At what level of exposure does collateral need to be posted. Will typically be zero for banks.  Should be stated in reference currency
    rounding_decimal_places=0,  # required — Where a calculation needs to be rounded to a specific number of decimal places,  this states the number that that requires.
    initial_margin_amount=0.0,  # required — The initial margin that is required. In the reference currency
    minimum_transfer_amount=0.0,  # required — The minimum amount, in the reference currency, that must be transferred when required.
    id=ResourceId(...)  # required
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

