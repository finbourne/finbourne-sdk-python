# UpsertInstrumentPropertyRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifier_type** | **str** | Required | The unique identifier type to search for the instrument, for example &#39;Figi&#39;. |
| **identifier** | **str** | Required | A value of that type to identify the instrument to upsert properties for, for example &#39;BBG000BLNNV0&#39;. |
| **properties** | [List[ModelProperty]](ModelProperty.md) | Optional | A set of instrument properties and associated values to store for the instrument. Each property must be from the &#39;Instrument&#39; domain. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertInstrumentPropertyRequest import UpsertInstrumentPropertyRequest

instance = UpsertInstrumentPropertyRequest(
    identifier_type="...",  # required — The unique identifier type to search for the instrument, for example &#39;Figi&#39;.
    identifier="...",  # required — A value of that type to identify the instrument to upsert properties for, for example &#39;BBG000BLNNV0&#39;.
    properties=[]  # optional — A set of instrument properties and associated values to store for the instrument. Each property must be from the &#39;Instrument&#39; domain.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

