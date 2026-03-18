# ManualEvent

Details of a manually triggered event
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **header** | [ManualEventHeader](ManualEventHeader.md) | Required | *No description available.* |
| **body** | [ManualEventBody](ManualEventBody.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.ManualEvent import ManualEvent

instance = ManualEvent(
    header=ManualEventHeader(...),  # required
    body=ManualEventBody(...)  # required
)
```


## Related Models

- [ManualEventHeader](ManualEventHeader.md)
- [ManualEventBody](ManualEventBody.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

