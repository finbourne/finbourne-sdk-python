# AvailableValue

A value known to be valid for a queryable log field, which a UI can offer when filtering on that field.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **str** | Required | The value. |
| **context** | **str** | Optional | Optional context qualifying the value. For the Operation field this is the comma-separated names of the applications that publish the operation. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.AvailableValue import AvailableValue

instance = AvailableValue(
    value="...",  # required — The value.
    context="..."  # optional — Optional context qualifying the value. For the Operation field this is the comma-separated names of the applications that publish the operation.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

