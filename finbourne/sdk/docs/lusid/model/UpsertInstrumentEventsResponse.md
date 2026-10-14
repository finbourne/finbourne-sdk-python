# UpsertInstrumentEventsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, InstrumentEventHolder]](InstrumentEventHolder.md) | Optional | The instrument events which have been successfully updated or inserted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The instrument events that could not be updated or inserted along with a reason for their failure. |
| **staged** | [Dict[str, InstrumentEventHolder]](InstrumentEventHolder.md) | Optional | The instrument events that have been staged pending approval. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInstrumentEventsResponse import UpsertInstrumentEventsResponse

instance = UpsertInstrumentEventsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=InstrumentEventHolder(...),  # optional — The instrument events which have been successfully updated or inserted.
    failed=ErrorDetail(...),  # optional — The instrument events that could not be updated or inserted along with a reason for their failure.
    staged=InstrumentEventHolder(...),  # optional — The instrument events that have been staged pending approval.
    links=[]  # optional
)
```

- [InstrumentEventHolder](InstrumentEventHolder.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [InstrumentEventHolder](InstrumentEventHolder.md) — used in `staged`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

