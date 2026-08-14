# SupplementalAttributeValues

A supplemental attribute value carried on a rec result for context. Does not contribute to matching.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **attribute_name** | **str** | Required | The name of the supplemental attribute. |
| **left_value** | **str** | Optional | The left-side value. |
| **right_value** | **str** | Optional | The right-side value. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SupplementalAttributeValues import SupplementalAttributeValues

instance = SupplementalAttributeValues(
    attribute_name="...",  # required — The name of the supplemental attribute.
    left_value="...",  # optional — The left-side value.
    right_value="..."  # optional — The right-side value.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

