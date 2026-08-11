# AddToPolicyCollectionRequest

Base properties to create or update a policy collection
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **policies** | [List[PolicyId]](PolicyId.md) | Optional | The identifiers of the Policies to be added to the collection. |
| **policy_collections** | [List[PolicyCollectionId]](PolicyCollectionId.md) | Optional | The identifiers of the PolicyCollections to be added to the collection. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.AddToPolicyCollectionRequest import AddToPolicyCollectionRequest

instance = AddToPolicyCollectionRequest(
    policies=[],  # optional — The identifiers of the Policies to be added to the collection.
    policy_collections=[]  # optional — The identifiers of the PolicyCollections to be added to the collection.
)
```


## Related Models

- [PolicyId](PolicyId.md) — used in `policies`
- [PolicyCollectionId](PolicyCollectionId.md) — used in `policy_collections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

