# AllocationEventNoticeLine

One line of a notice: an amount allocated to the partner under an ILPA transaction type.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **ilpa_transaction_type** | **str** | Required | The ILPA transaction type of the line. |
| **component** | **str** | Optional | The allocation event component the line is for. |
| **inside_fund** | **bool** | Required | Whether the line moves capital inside the fund, as opposed to a fee or expense outside it. |
| **amount** | **float** | Required | The amount of the line. |
| **unfunded_impact** | **float** | Required | The effect of the line on the partner&#39;s unfunded commitment. |
| **recallable_until** | **datetime** | Optional | The date until which a recallable distribution may be recalled, or null. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventNoticeLine import AllocationEventNoticeLine

instance = AllocationEventNoticeLine(
    ilpa_transaction_type="...",  # required — The ILPA transaction type of the line.
    component="...",  # optional — The allocation event component the line is for.
    inside_fund=True,  # required — Whether the line moves capital inside the fund, as opposed to a fee or expense outside it.
    amount=0.0,  # required — The amount of the line.
    unfunded_impact=0.0,  # required — The effect of the line on the partner&#39;s unfunded commitment.
    recallable_until=datetime.now()  # optional — The date until which a recallable distribution may be recalled, or null.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

