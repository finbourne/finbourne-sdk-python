# A2BBreakdown

A2B Breakdown - Shows the total, and each sub-element within an A2B Category
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **total** | **float** | Optional | The total value of all the components within this category. |
| **currency** | **str** | Optional | The currency. Applies to the Total, as well as all the componenents. |
| **components** | **Dict[str, float]** | Optional | The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.A2BBreakdown import A2BBreakdown

instance = A2BBreakdown(
    total=0.0,  # optional — The total value of all the components within this category.
    currency="...",  # optional — The currency. Applies to the Total, as well as all the componenents.
    components=  # optional — The individual components that make up the category. For example, the Start category may have Cost, Unrealised gains and accrued interest components.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

