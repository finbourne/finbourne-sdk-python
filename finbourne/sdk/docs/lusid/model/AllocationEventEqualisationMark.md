# AllocationEventEqualisationMark

A valuation move already allocated to the existing partners that the close re-trues to the admitted partners.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **origin_member_short_code** | **str** | Required | The member of the structure the mark belongs to. |
| **amount** | **float** | Required | The valuation move already allocated, in the event currency. Negative for a fall in value or an expense. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventEqualisationMark import AllocationEventEqualisationMark

instance = AllocationEventEqualisationMark(
    origin_member_short_code="...",  # required — The member of the structure the mark belongs to.
    amount=0.0  # required — The valuation move already allocated, in the event currency. Negative for a fall in value or an expense.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

