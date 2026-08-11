# PortfolioCashLadder

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **currency** | **str** | Required | The currency of the cash-flows. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. |
| **records** | [List[CashLadderRecord]](CashLadderRecord.md) | Required | A record of cash flows on a specific date. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The records that could not be returned along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioCashLadder import PortfolioCashLadder

instance = PortfolioCashLadder(
    currency="...",  # required — The currency of the cash-flows.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio.
    records=[],  # required — A record of cash flows on a specific date.
    failed=ErrorDetail(...),  # optional — The records that could not be returned along with a reason for their failure.
    links=[]  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [CashLadderRecord](CashLadderRecord.md) — used in `records`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

