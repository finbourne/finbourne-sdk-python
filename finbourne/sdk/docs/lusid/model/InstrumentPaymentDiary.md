# InstrumentPaymentDiary

A payment diary containing all the cashflows on a single instrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_id_type** | **str** | Optional | The identifier type of the instrument. |
| **instrument_id** | **str** | Optional | The identifier for the instrument. |
| **instrument_scope** | **str** | Optional | The scope of the instrument. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **legs** | [List[InstrumentPaymentDiaryLeg]](InstrumentPaymentDiaryLeg.md) | Optional | Aggregated sets of Cashflows. |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentPaymentDiary import InstrumentPaymentDiary

instance = InstrumentPaymentDiary(
    instrument_id_type="...",  # optional — The identifier type of the instrument.
    instrument_id="...",  # optional — The identifier for the instrument.
    instrument_scope="...",  # optional — The scope of the instrument.
    version=Version(...),  # optional
    legs=[],  # optional — Aggregated sets of Cashflows.
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    links=[]  # optional
)
```

- [Version](Version.md)
- [InstrumentPaymentDiaryLeg](InstrumentPaymentDiaryLeg.md) — used in `legs`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

