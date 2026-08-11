# StructuredResultData

An item of structured result data that is to be inserted into Lusid. This will typically be a Json or Xml document that  contains a set of result data appropriate to a specific entity such as an instrument or potentially an index.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **document_format** | **str** | Required | The format of the accompanying document. |
| **version** | **str** | Optional | The semantic version of the document format; MAJOR.MINOR.PATCH |
| **name** | **str** | Optional | The name or description for the document |
| **document** | **str** | Required | The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields |
| **data_map_key** | [DataMapKey](DataMapKey.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StructuredResultData import StructuredResultData

instance = StructuredResultData(
    document_format="...",  # required — The format of the accompanying document.
    version="...",  # optional — The semantic version of the document format; MAJOR.MINOR.PATCH
    name="...",  # optional — The name or description for the document
    document="...",  # required — The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields
    data_map_key=DataMapKey(...)  # optional
)
```

- [DataMapKey](DataMapKey.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

