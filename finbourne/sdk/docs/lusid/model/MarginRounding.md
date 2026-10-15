# MarginRounding

The increment margin calls are rounded to, and the direction for deliveries and returns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amount** | **float** | Required | The increment margin calls are rounded to. Must be greater than zero. |
| **deliveries** | **str** | Required | How amounts we deliver are rounded. One of Up or Nearest. Available values: Up, Down, Nearest. |
| **returns** | **str** | Required | How amounts we receive back are rounded. One of Down or Nearest. Available values: Up, Down, Nearest. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginRounding import MarginRounding

instance = MarginRounding(
    amount=0.0,  # required — The increment margin calls are rounded to. Must be greater than zero.
    deliveries="...",  # required — How amounts we deliver are rounded. One of Up or Nearest. Available values: Up, Down, Nearest.
    returns="..."  # required — How amounts we receive back are rounded. One of Down or Nearest. Available values: Up, Down, Nearest.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

