# ParameterValue

Defines a Parameter Value
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | Name |
| **value** | **object** | Optional | Value which can be a String, Boolean, Decimal or DateTime (ISO 8601) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ParameterValue import ParameterValue

instance = ParameterValue(
    name="...",  # required — Name
    value=  # optional — Value which can be a String, Boolean, Decimal or DateTime (ISO 8601)
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

