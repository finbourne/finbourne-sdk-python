# InstantiateRecRequest

The request to instantiate a new rec instance from a rec definition and start its first run. Each  date accepts a date-time or a LUSID cut label, and defaults to the current date-time when omitted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rec_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **left_effective_at** | **str** | Optional | The left effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. |
| **left_as_at** | **str** | Optional | The left asAt datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. |
| **right_effective_at** | **str** | Optional | The right effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. |
| **right_as_at** | **str** | Optional | The right asAt datetime, as a date-time or a LUSID cut label. Defaults to the current date-time. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstantiateRecRequest import InstantiateRecRequest

instance = InstantiateRecRequest(
    rec_definition_id=ResourceId(...),  # required
    left_effective_at="...",  # optional — The left effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time.
    left_as_at="...",  # optional — The left asAt datetime, as a date-time or a LUSID cut label. Defaults to the current date-time.
    right_effective_at="...",  # optional — The right effective datetime, as a date-time or a LUSID cut label. Defaults to the current date-time.
    right_as_at="..."  # optional — The right asAt datetime, as a date-time or a LUSID cut label. Defaults to the current date-time.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

