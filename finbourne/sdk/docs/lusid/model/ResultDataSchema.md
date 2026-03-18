# ResultDataSchema

The shape and type of the returned data. The AddressSchema gives information about the requested keys,  including the return type, links to further documentation, lifecycle status and removal date if they are  deprecated.                Note: the NodeValueSchema and PropertySchema fields have been deprecated. Please use the AddressSchema instead.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **node_value_schema** | [Dict[str, FieldSchema]](FieldSchema.md) | Optional | This has been deprecated. Please use AddressSchema instead. |
| **property_schema** | [Dict[str, FieldSchema]](FieldSchema.md) | Optional | This has been deprecated. Please use AddressSchema instead. |
| **address_schema** | [Dict[str, AddressDefinition]](AddressDefinition.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultDataSchema import ResultDataSchema

instance = ResultDataSchema(
    node_value_schema=FieldSchema(...),  # optional — This has been deprecated. Please use AddressSchema instead.
    property_schema=FieldSchema(...),  # optional — This has been deprecated. Please use AddressSchema instead.
    address_schema=AddressDefinition(...)  # optional
)
```


## Related Models

- [FieldSchema](FieldSchema.md) — used in `node_value_schema`
- [FieldSchema](FieldSchema.md) — used in `property_schema`
- [AddressDefinition](AddressDefinition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

