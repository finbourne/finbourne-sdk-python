# InstrumentModels

Supported pricing models for an instrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_id** | **str** | Optional | The unique LUSID Instrument Identifier (LUID) of the instrument. |
| **supported_models** | **List[str]** | Optional | The pricing models supported by the instrument e.g. &#39;Discounting&#39;. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentModels import InstrumentModels

instance = InstrumentModels(
    instrument_id="...",  # optional — The unique LUSID Instrument Identifier (LUID) of the instrument.
    supported_models=,  # optional — The pricing models supported by the instrument e.g. &#39;Discounting&#39;.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

