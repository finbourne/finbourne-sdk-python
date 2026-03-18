# CreateDateRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **date_id** | **str** | Required | *No description available.* |
| **from_utc** | **datetime** | Required | *No description available.* |
| **to_utc** | **datetime** | Required | *No description available.* |
| **time_zone** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **type** | **str** | Optional | *No description available.* |
| **attributes** | [DateAttributes](DateAttributes.md) | Optional | *No description available.* |
| **source_data** | **Dict[str, Optional[str]]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateDateRequest import CreateDateRequest

instance = CreateDateRequest(
    date_id="...",  # required
    from_utc=datetime.now(),  # required
    to_utc=datetime.now(),  # required
    time_zone="...",  # required
    description="...",  # required
    type="...",  # optional
    attributes=DateAttributes(...),  # optional
    source_data=  # optional
)
```

- [DateAttributes](DateAttributes.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

