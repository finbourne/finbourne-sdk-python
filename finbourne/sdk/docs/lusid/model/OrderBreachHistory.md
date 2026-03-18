# OrderBreachHistory

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **run_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **breaches_by_rule** | **Dict[str, Optional[List[OrderRuleBreach]]]** | Optional | Compliance rule breaches associations with the order and run. |
| **as_at** | **datetime** | Required | The asAt datetime at which the order breach was created in LUSID. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderBreachHistory import OrderBreachHistory

instance = OrderBreachHistory(
    id=ResourceId(...),  # required
    order_id=ResourceId(...),  # required
    run_id=ResourceId(...),  # required
    breaches_by_rule=,  # optional — Compliance rule breaches associations with the order and run.
    as_at=datetime.now()  # required — The asAt datetime at which the order breach was created in LUSID.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

