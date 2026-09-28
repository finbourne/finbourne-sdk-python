# AllocationEventReallocateRequest

The request used to recompute an unbooked Allocation Event: why, and with which basis values.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reason** | **str** | Required | Why the event is being recomputed. |
| **basis_values** | [List[AllocationMapBasisValue]](AllocationMapBasisValue.md) | Optional | Optional replacement basis values per investor record. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventReallocateRequest import AllocationEventReallocateRequest

instance = AllocationEventReallocateRequest(
    reason="...",  # required — Why the event is being recomputed.
    basis_values=[]  # optional — Optional replacement basis values per investor record.
)
```

- [AllocationMapBasisValue](AllocationMapBasisValue.md) — used in `basis_values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

