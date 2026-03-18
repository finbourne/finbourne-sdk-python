# UpsertInstrumentsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, Instrument]](Instrument.md) | Optional | The instruments which have been successfully updated or created. |
| **staged** | [Dict[str, Instrument]](Instrument.md) | Optional | The instruments that have been staged for updation or creation. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Meta data associated with the upsert event. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInstrumentsResponse import UpsertInstrumentsResponse

instance = UpsertInstrumentsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=Instrument(...),  # optional — The instruments which have been successfully updated or created.
    staged=Instrument(...),  # optional — The instruments that have been staged for updation or creation.
    failed=ErrorDetail(...),  # optional — The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure.
    metadata=,  # optional — Meta data associated with the upsert event.
    links=[]  # optional
)
```

- [Instrument](Instrument.md) — used in `values`
- [Instrument](Instrument.md) — used in `staged`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

