# PolicyCollectionResponse

A PolicyCollection encapsulating one or more Policies and PolicyCollections
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [PolicyCollectionId](PolicyCollectionId.md) | Optional | *No description available.* |
| **policies** | [List[PolicyId]](PolicyId.md) | Optional | The identifiers of the Policies in this collection |
| **policy_collections** | [List[PolicyCollectionId]](PolicyCollectionId.md) | Optional | The identifiers of the PolicyCollections in this collection |
| **description** | **str** | Optional | A description of this policy collection |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.PolicyCollectionResponse import PolicyCollectionResponse

instance = PolicyCollectionResponse(
    id=PolicyCollectionId(...),  # optional
    policies=[],  # optional — The identifiers of the Policies in this collection
    policy_collections=[],  # optional — The identifiers of the PolicyCollections in this collection
    description="...",  # optional — A description of this policy collection
    links=[]  # optional
)
```


## Related Models

- [PolicyCollectionId](PolicyCollectionId.md)
- [PolicyId](PolicyId.md) — used in `policies`
- [PolicyCollectionId](PolicyCollectionId.md) — used in `policy_collections`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

