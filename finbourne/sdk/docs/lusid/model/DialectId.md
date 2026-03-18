# DialectId

Unique identifier of a given Dialect
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The Scope of the dialect. |
| **vendor** | **str** | Required | The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE. |
| **source_system** | **str** | Required | The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib. |
| **version** | **str** | Required | The semantic version of the dialect: MAJOR.MINOR.PATCH. |
| **serialisation_format** | **str** | Required | The serialisation format of a document in this dialect. e.g. JSON, XML. |
| **entity_type** | **str** | Required | The type of entity this dialect describes e.g. Instrument. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DialectId import DialectId

instance = DialectId(
    scope="...",  # required — The Scope of the dialect.
    vendor="...",  # required — The vendor of the dialect, the entity that created it. e.g. ISDA, FINBOURNE.
    source_system="...",  # required — The source system of the dialect, the system that understands it. e.g. LUSID, QuantLib.
    version="...",  # required — The semantic version of the dialect: MAJOR.MINOR.PATCH.
    serialisation_format="...",  # required — The serialisation format of a document in this dialect. e.g. JSON, XML.
    entity_type="..."  # required — The type of entity this dialect describes e.g. Instrument.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

