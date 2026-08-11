# CustodianEntry

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **account_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **account_selector** | **str** | Optional | Available values: From, To. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustodianEntry import CustodianEntry

instance = CustodianEntry(
    account_id=ResourceId(...),  # required
    account_selector="..."  # optional — Available values: From, To.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

