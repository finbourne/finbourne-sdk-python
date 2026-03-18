# DiaryEntry

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **abor_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **diary_entry_code** | **str** | Optional | The code of the diary entry. |
| **type** | **str** | Required | The type of the diary entry. |
| **name** | **str** | Optional | The name of the diary entry. |
| **status** | **str** | Required | The status of the diary entry. Statuses are constrained and defaulted by &#39;Type&#39; specified.   Type &#39;Other&#39; defaults to &#39;Undefined&#39; and supports &#39;Undefined&#39;, &#39;Estimate&#39;, &#39;Candidate&#39;, and &#39;Final&#39;.  Type &#39;PeriodBoundary&#39; defaults to &#39;Estimate&#39; when closing a period, and supports &#39;Estimate&#39; and &#39;Final&#39; for closing periods and &#39;Final&#39; for locking periods.  Type &#39;ValuationPoint&#39; defaults to &#39;Estimate&#39; when upserting a diary entry, moves to &#39;Candidate&#39; or &#39;Final&#39; when a ValuationPoint is accepted, and &#39;Final&#39; when it is finalised. |
| **apply_clear_down** | **bool** | Optional | Defaults to false. Set to true if you want that the closed period to have the clear down applied. |
| **effective_at** | **datetime** | Required | The effective time of the diary entry. |
| **query_as_at** | **datetime** | Optional | The query time of the diary entry. Defaults to latest. |
| **previous_entry_time** | **datetime** | Optional | The entry time of the previous diary entry. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the diary entry. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DiaryEntry import DiaryEntry

instance = DiaryEntry(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    abor_id=ResourceId(...),  # optional
    diary_entry_code="...",  # optional — The code of the diary entry.
    type="...",  # required — The type of the diary entry.
    name="...",  # optional — The name of the diary entry.
    status="...",  # required — The status of the diary entry. Statuses are constrained and defaulted by &#39;Type&#39; specified.   Type &#39;Other&#39; defaults to &#39;Undefined&#39; and supports &#39;Undefined&#39;, &#39;Estimate&#39;, &#39;Candidate&#39;, and &#39;Final&#39;.  Type &#39;PeriodBoundary&#39; defaults to &#39;Estimate&#39; when closing a period, and supports &#39;Estimate&#39; and &#39;Final&#39; for closing periods and &#39;Final&#39; for locking periods.  Type &#39;ValuationPoint&#39; defaults to &#39;Estimate&#39; when upserting a diary entry, moves to &#39;Candidate&#39; or &#39;Final&#39; when a ValuationPoint is accepted, and &#39;Final&#39; when it is finalised.
    apply_clear_down=True,  # optional — Defaults to false. Set to true if you want that the closed period to have the clear down applied.
    effective_at=datetime.now(),  # required — The effective time of the diary entry.
    query_as_at=datetime.now(),  # optional — The query time of the diary entry. Defaults to latest.
    previous_entry_time=datetime.now(),  # optional — The entry time of the previous diary entry.
    properties=ModelProperty(...),  # optional — A set of properties for the diary entry.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

