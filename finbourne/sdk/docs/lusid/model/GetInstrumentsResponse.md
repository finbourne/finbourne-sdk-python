# GetInstrumentsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, Instrument]](Instrument.md) | Optional | The instrument definitions, keyed by the identifier used to retrieve them. Only instruments that were found will be contained in this collection. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The identifiers that did not resolve to an instrument along with the nature of the failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetInstrumentsResponse import GetInstrumentsResponse

instance = GetInstrumentsResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=Instrument(...),  # optional — The instrument definitions, keyed by the identifier used to retrieve them. Only instruments that were found will be contained in this collection.
    failed=ErrorDetail(...),  # optional — The identifiers that did not resolve to an instrument along with the nature of the failure.
    links=[]  # optional
)
```

- [Instrument](Instrument.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

