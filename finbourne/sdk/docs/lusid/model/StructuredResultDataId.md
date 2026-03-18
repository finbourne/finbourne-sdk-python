# StructuredResultDataId

An identifier that uniquely describes an item of structured result data such as the risk to an interest curve or a set of yields or analytics on an index.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source** | **str** | Required | The platform or vendor that provided the structured result data, e.g. &#39;client&#39;. This is primarily of interest when data could have been sourced from multiple sources |
| **code** | **str** | Optional | The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data |
| **effective_at** | **str** | Optional | The effectiveAt or cut label that this item of structured result data is/was updated/inserted with. |
| **result_type** | **str** | Optional | An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as &#39;risk result&#39;, &#39;cashflow&#39;, &#39;index&#39; or similar. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StructuredResultDataId import StructuredResultDataId

instance = StructuredResultDataId(
    source="...",  # required — The platform or vendor that provided the structured result data, e.g. &#39;client&#39;. This is primarily of interest when data could have been sourced from multiple sources
    code="...",  # optional — The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data
    effective_at="...",  # optional — The effectiveAt or cut label that this item of structured result data is/was updated/inserted with.
    result_type="..."  # optional — An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as &#39;risk result&#39;, &#39;cashflow&#39;, &#39;index&#39; or similar.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

