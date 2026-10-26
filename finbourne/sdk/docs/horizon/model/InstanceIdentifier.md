# InstanceIdentifier

Identifies a single instance of an integration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | Instance identifier. |
| **warnings** | [List[ValidationNoticeResponse]](ValidationNoticeResponse.md) | Optional | Non-blocking findings about the saved configuration. Empty when there are none. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.InstanceIdentifier import InstanceIdentifier

instance = InstanceIdentifier(
    id="...",  # required — Instance identifier.
    warnings=[]  # optional — Non-blocking findings about the saved configuration. Empty when there are none.
)
```

- [ValidationNoticeResponse](ValidationNoticeResponse.md) — used in `warnings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

