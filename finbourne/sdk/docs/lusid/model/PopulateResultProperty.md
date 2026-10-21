# PopulateResultProperty

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **property_key** | **str** | Required | The property the formula populates. Must be an existing, single-valued property in the RecResult domain, and may appear only once. |
| **formula** | **str** | Required | The formula whose value populates the property; a null value means the property has no value. |
| **overwrite_manual_edits_on_re_run** | **bool** | Optional | Whether a value edited since the property was last populated is replaced. Defaults to false, so manual edits are kept. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PopulateResultProperty import PopulateResultProperty

instance = PopulateResultProperty(
    property_key="...",  # required — The property the formula populates. Must be an existing, single-valued property in the RecResult domain, and may appear only once.
    formula="...",  # required — The formula whose value populates the property; a null value means the property has no value.
    overwrite_manual_edits_on_re_run=True  # optional — Whether a value edited since the property was last populated is replaced. Defaults to false, so manual edits are kept.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

