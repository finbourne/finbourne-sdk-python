# AllocationMapBasisValue

The value one investor record is weighted by when an Allocation Map is resolved.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the basis value belongs to. |
| **basis_value** | **float** | Required | The value the investor record is weighted by, for example its commitment. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapBasisValue import AllocationMapBasisValue

instance = AllocationMapBasisValue(
    investor_record_id="...",  # required — The investor record the basis value belongs to.
    basis_value=0.0  # required — The value the investor record is weighted by, for example its commitment.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

