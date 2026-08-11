# UpsertInstrumentPropertiesResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at_date** | **datetime** | Required | The as-at datetime at which properties were created or updated. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInstrumentPropertiesResponse import UpsertInstrumentPropertiesResponse

instance = UpsertInstrumentPropertiesResponse(
    as_at_date=datetime.now(),  # required — The as-at datetime at which properties were created or updated.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

