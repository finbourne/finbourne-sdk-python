# Participation

The record an order's participation in a specific placement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **placement_id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **order_id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **version** | [../model/Version](Version.md) | Optional | *No description available.* |
| **data_model_membership** | [../model/DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Participation import Participation

instance = Participation(
    id=ResourceId(...),  # required
    placement_id=ResourceId(...),  # required
    order_id=ResourceId(...),  # required
    version=Version(...),  # optional
    data_model_membership=DataModelMembership(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Version](Version.md)
- [DataModelMembership](DataModelMembership.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

