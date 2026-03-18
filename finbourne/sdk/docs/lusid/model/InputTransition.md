# InputTransition

The input 'transition' within a corporate action, representing the singular input position
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **units_factor** | **float** | Required | The factor to scale units by |
| **cost_factor** | **float** | Required | The factor to scale cost by |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InputTransition import InputTransition

instance = InputTransition(
    units_factor=0.0,  # required — The factor to scale units by
    cost_factor=0.0  # required — The factor to scale cost by
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

