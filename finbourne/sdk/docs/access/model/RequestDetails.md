# RequestDetails

The details of the requested evaluation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **action** | [RequestedActionKey](RequestedActionKey.md) | Required | *No description available.* |
| **from_effective_date** | **datetime** | Optional | The start date for the requested effective date range for the resource (if null, UtcNow) |
| **to_effective_date** | **datetime** | Optional | The end date for the requested effective date range for the resource (if null, same as from date) |
| **from_as_at** | **datetime** | Optional | The requested AsAt date for the resource (if null, Latest). If specifying a range of AsAt dates, this is the lower bounds. |
| **to_as_at** | **datetime** | Optional | Upper bound if specifying a request that requires a range of AsAt dates. This is used if specifying the desire to grant access for a user between an AsAt range. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.RequestDetails import RequestDetails

instance = RequestDetails(
    action=RequestedActionKey(...),  # required
    from_effective_date=datetime.now(),  # optional — The start date for the requested effective date range for the resource (if null, UtcNow)
    to_effective_date=datetime.now(),  # optional — The end date for the requested effective date range for the resource (if null, same as from date)
    from_as_at=datetime.now(),  # optional — The requested AsAt date for the resource (if null, Latest). If specifying a range of AsAt dates, this is the lower bounds.
    to_as_at=datetime.now()  # optional — Upper bound if specifying a request that requires a range of AsAt dates. This is used if specifying the desire to grant access for a user between an AsAt range.
)
```


## Related Models

- [RequestedActionKey](RequestedActionKey.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

