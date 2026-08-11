# PolicyCollectionCreationRequest

Create a PolicyCollection, a logical group of Policies or other PolicyCollections
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The identifier for the PolicyCollection being created |
| **policies** | [List[PolicyId]](PolicyId.md) | Optional | The identifiers of the Policies in this collection |
| **metadata** | **Dict[str, Optional[List[EntitlementMetadata]]]** | Optional | Any relevant metadata associated with this resource for controlling access to this resource |
| **policy_collections** | [List[PolicyCollectionId]](PolicyCollectionId.md) | Optional | The identifiers of the PolicyCollections in this collection |
| **description** | **str** | Optional | A description of this policy collection |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.PolicyCollectionCreationRequest import PolicyCollectionCreationRequest

instance = PolicyCollectionCreationRequest(
    code="...",  # required — The identifier for the PolicyCollection being created
    policies=[],  # optional — The identifiers of the Policies in this collection
    metadata=,  # optional — Any relevant metadata associated with this resource for controlling access to this resource
    policy_collections=[],  # optional — The identifiers of the PolicyCollections in this collection
    description="..."  # optional — A description of this policy collection
)
```

- [PolicyId](PolicyId.md) — used in `policies`
- [PolicyCollectionId](PolicyCollectionId.md) — used in `policy_collections`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

