# OptionsXml

Additional options applicable to the given SourceType
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **column_types** | **str** | Optional | Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified) |
| **infer_type_row_count** | **int** | Optional | If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified |
| **values_to_make_null** | **str** | Optional | Regex of values to map to &#39;null&#39; in the returned data. |
| **column_names** | **str** | Optional | Column Names either overrides the header row or steps in when there is no header row (comma delimited list) |
| **node_path** | **str** | Optional | XPath query that selects the nodes to map to rows |
| **namespaces** | **str** | Optional | Selected prefix(es) and namespace(s):prefix1&#x3D;namespace1-uri1,prefix2&#x3D;namespace2-uri2,...prefixN&#x3D;namespaceN-uriN |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.OptionsXml import OptionsXml

instance = OptionsXml(
    column_types="...",  # optional — Column types (comma delimited list of: &#39;{types}&#39;, some columns may be left blank while others are specified)
    infer_type_row_count=0,  # optional — If non-zero and &#39;types&#39; is not specified (or not specified for some columns) this will look through N rows to attempt to work out the column types for columns not pre-specified
    values_to_make_null="...",  # optional — Regex of values to map to &#39;null&#39; in the returned data.
    column_names="...",  # optional — Column Names either overrides the header row or steps in when there is no header row (comma delimited list)
    node_path="...",  # optional — XPath query that selects the nodes to map to rows
    namespaces="..."  # optional — Selected prefix(es) and namespace(s):prefix1&#x3D;namespace1-uri1,prefix2&#x3D;namespace2-uri2,...prefixN&#x3D;namespaceN-uriN
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

