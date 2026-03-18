# Dialect

The language/format of a translatable entity. Entities can be LUSID native or external and the Dialect describes  1) the system that understands the entity and  2) applicable validation for the entity, in the form of a schema.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [DialectId](DialectId.md) | Required | *No description available.* |
| **var_schema** | [DialectSchema](DialectSchema.md) | Required | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Dialect import Dialect

instance = Dialect(
    id=DialectId(...),  # required
    var_schema=DialectSchema(...),  # required
    version=Version(...)  # optional
)
```


## Related Models

- [DialectId](DialectId.md)
- [DialectSchema](DialectSchema.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

