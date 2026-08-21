# ResultAxisDefinition

Describes one labelled axis of a matrix-shaped result (Result1D/Result2D), so consumers can  tell what the labels on that axis mean without opening each value.  A Result1D has a single Y axis; a Result2D has a Y (row) and an X (column) axis.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **axis** | **str** | Optional | Which axis of the result this describes: \&quot;Y\&quot; labels the rows (the only axis of a Result1D,  serialized as labelsY on the value); \&quot;X\&quot; labels the columns of a Result2D (labelsX). |
| **name** | **str** | Optional | The display name of the axis, e.g. \&quot;Bucket\&quot; or \&quot;Expiry\&quot;. |
| **label_type** | **str** | Optional | What kind of value the axis labels are drawn from, e.g. \&quot;Tenor\&quot;, \&quot;Date\&quot; or \&quot;Strike\&quot;.  Consumers can switch rendering on well-known values and fall back to showing labels verbatim. |
| **description** | **str** | Optional | What the axis means for this result. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultAxisDefinition import ResultAxisDefinition

instance = ResultAxisDefinition(
    axis="...",  # optional — Which axis of the result this describes: \&quot;Y\&quot; labels the rows (the only axis of a Result1D,  serialized as labelsY on the value); \&quot;X\&quot; labels the columns of a Result2D (labelsX).
    name="...",  # optional — The display name of the axis, e.g. \&quot;Bucket\&quot; or \&quot;Expiry\&quot;.
    label_type="...",  # optional — What kind of value the axis labels are drawn from, e.g. \&quot;Tenor\&quot;, \&quot;Date\&quot; or \&quot;Strike\&quot;.  Consumers can switch rendering on well-known values and fall back to showing labels verbatim.
    description="..."  # optional — What the axis means for this result.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

