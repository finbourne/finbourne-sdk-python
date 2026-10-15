# EligibleCollateralReferences

The eligible collateral schedule each party's posting is checked against.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **we_post** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **they_post** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EligibleCollateralReferences import EligibleCollateralReferences

instance = EligibleCollateralReferences(
    we_post=ResourceId(...),  # optional
    they_post=ResourceId(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

