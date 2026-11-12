# ChargeableGainsTakeOn

Carried-forward chargeable-gains balances for a tax-lot taken on under the UK chargeable gains accounting method
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **role** | **str** | Required | Available values: Section104Pool, Holding1982, Holding1965. |
| **indexation** | **float** | Optional | *No description available.* |
| **indexed_to** | **datetime** | Optional | *No description available.* |
| **original_cost** | **float** | Optional | *No description available.* |
| **market_value1982** | **float** | Optional | *No description available.* |
| **rebasing_election** | **bool** | Optional | *No description available.* |
| **additions** | [List[ChargeableGainsTakeOnAddition]](ChargeableGainsTakeOnAddition.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ChargeableGainsTakeOn import ChargeableGainsTakeOn

instance = ChargeableGainsTakeOn(
    role="...",  # required — Available values: Section104Pool, Holding1982, Holding1965.
    indexation=0.0,  # optional
    indexed_to=datetime.now(),  # optional
    original_cost=0.0,  # optional
    market_value1982=0.0,  # optional
    rebasing_election=True,  # optional
    additions=[]  # optional
)
```

- [ChargeableGainsTakeOnAddition](ChargeableGainsTakeOnAddition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

