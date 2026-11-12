# TaxExceptionRootCause

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | A stable code for the cause, for example PoolOutOfSync or MissingTreatmentLeaf. |
| **label** | **str** | Required | A display label for the cause. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxExceptionRootCause import TaxExceptionRootCause

instance = TaxExceptionRootCause(
    code="...",  # required — A stable code for the cause, for example PoolOutOfSync or MissingTreatmentLeaf.
    label="..."  # required — A display label for the cause.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

