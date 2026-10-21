# InstrumentEventInstructionsResponse

The collection of successfully upserted instructions, the collection of those staged pending approval, and the collection of failures for those instructions that could not be upserted
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, InstrumentEventInstruction]](InstrumentEventInstruction.md) | Optional | The collection of successfully upserted instructions |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The collection of error information for instructions that could not be upserted |
| **staged** | [Dict[str, InstrumentEventInstruction]](InstrumentEventInstruction.md) | Optional | The instructions that have been staged pending approval. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentEventInstructionsResponse import InstrumentEventInstructionsResponse

instance = InstrumentEventInstructionsResponse(
    values=InstrumentEventInstruction(...),  # optional — The collection of successfully upserted instructions
    failed=ErrorDetail(...),  # optional — The collection of error information for instructions that could not be upserted
    staged=InstrumentEventInstruction(...)  # optional — The instructions that have been staged pending approval.
)
```


## Related Models

- [InstrumentEventInstruction](InstrumentEventInstruction.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [InstrumentEventInstruction](InstrumentEventInstruction.md) — used in `staged`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

