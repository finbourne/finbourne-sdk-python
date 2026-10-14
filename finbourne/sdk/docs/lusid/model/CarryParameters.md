# CarryParameters

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **carry_rate** | **float** | Required | *No description available.* |
| **preferred_return_rate** | **float** | Optional | *No description available.* |
| **catch_up_rate** | **float** | Optional | *No description available.* |
| **waterfall_type** | **str** | Optional | Available values: WholeOfFund, DealByDeal. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CarryParameters import CarryParameters

instance = CarryParameters(
    carry_rate=0.0,  # required
    preferred_return_rate=0.0,  # optional
    catch_up_rate=0.0,  # optional
    waterfall_type="..."  # optional — Available values: WholeOfFund, DealByDeal.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

