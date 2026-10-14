# FundClosing

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **closing_id** | **str** | Required | *No description available.* |
| **closing_date** | **datetime** | Required | *No description available.* |
| **is_final** | **bool** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundClosing import FundClosing

instance = FundClosing(
    closing_id="...",  # required
    closing_date=datetime.now(),  # required
    is_final=True,  # optional
    description="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

