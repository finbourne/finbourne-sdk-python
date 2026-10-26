# UpdateInstanceResponse

The outcome of updating an instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **warnings** | [List[ValidationNoticeResponse]](ValidationNoticeResponse.md) | Optional | Non-blocking findings about the saved configuration. Empty when there are none. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.UpdateInstanceResponse import UpdateInstanceResponse

instance = UpdateInstanceResponse(
    warnings=[]  # optional — Non-blocking findings about the saved configuration. Empty when there are none.
)
```


## Related Models

- [ValidationNoticeResponse](ValidationNoticeResponse.md) — used in `warnings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

