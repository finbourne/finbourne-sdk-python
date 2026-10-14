# StructuredResultDataResult

Represents structured result data document and row details for a data quality check result.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Optional | The type of the entity, e.g. \&quot;SrsRow\&quot;. |
| **as_at** | **datetime** | Optional | The as-at timestamp the document was read at |
| **effective_at** | **datetime** | Optional | The effective-at timestamp the document was read at |
| **document_effective_at** | **datetime** | Optional | The effective date of the upload the row was read from: the latest upload at or before effectiveAt |
| **scope** | **str** | Optional | The scope of the document |
| **code** | **str** | Optional | The code of the document |
| **source** | **str** | Optional | The platform or vendor that provided the document |
| **result_type** | **str** | Optional | The document&#39;s result type |
| **row_identifiers** | **Dict[str, Optional[str]]** | Optional | The row&#39;s identifier columns, keyed by address key. Populated when entityType is \&quot;SrsRow\&quot;. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StructuredResultDataResult import StructuredResultDataResult

instance = StructuredResultDataResult(
    entity_type="...",  # optional — The type of the entity, e.g. \&quot;SrsRow\&quot;.
    as_at=datetime.now(),  # optional — The as-at timestamp the document was read at
    effective_at=datetime.now(),  # optional — The effective-at timestamp the document was read at
    document_effective_at=datetime.now(),  # optional — The effective date of the upload the row was read from: the latest upload at or before effectiveAt
    scope="...",  # optional — The scope of the document
    code="...",  # optional — The code of the document
    source="...",  # optional — The platform or vendor that provided the document
    result_type="...",  # optional — The document&#39;s result type
    row_identifiers=  # optional — The row&#39;s identifier columns, keyed by address key. Populated when entityType is \&quot;SrsRow\&quot;.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

