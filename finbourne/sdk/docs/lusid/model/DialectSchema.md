# DialectSchema

A schema that a given document must obey. A representation of the validation of a particular Dialect,  in a given language.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of schema this represents |
| **body** | **str** | Optional | The body of the schema |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DialectSchema import DialectSchema

instance = DialectSchema(
    type="...",  # required — The type of schema this represents
    body="..."  # optional — The body of the schema
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

