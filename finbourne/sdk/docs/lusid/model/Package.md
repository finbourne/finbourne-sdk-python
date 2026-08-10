# Package

A structure used to describe the structure of an order or orders that make up a non-trivial trade.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **order_ids** | [../model/List[ResourceId]](ResourceId.md) | Required | Related order ids. |
| **order_instruction_ids** | [../model/List[ResourceId]](ResourceId.md) | Required | Related order instruction ids. |
| **properties** | [../model/Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this execution. |
| **version** | [../model/Version](Version.md) | Optional | *No description available.* |
| **data_model_membership** | [../model/DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Package import Package

instance = Package(
    id=ResourceId(...),  # required
    order_ids=[],  # required — Related order ids.
    order_instruction_ids=[],  # required — Related order instruction ids.
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this execution.
    version=Version(...),  # optional
    data_model_membership=DataModelMembership(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `order_ids`
- [ResourceId](ResourceId.md) — used in `order_instruction_ids`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [Version](Version.md)
- [DataModelMembership](DataModelMembership.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

