# VendorProduct

Denormalised information about vendors, the products they provide and the LUSID entity types they can be used to populate.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **vendor_name** | **str** | Required | *No description available.* |
| **product_name** | **str** | Required | *No description available.* |
| **vendor_product_key** | **str** | Required | *No description available.* |
| **lusid_entity** | [LusidEntity](LusidEntity.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.VendorProduct import VendorProduct

instance = VendorProduct(
    vendor_name="...",  # required
    product_name="...",  # required
    vendor_product_key="...",  # required
    lusid_entity=LusidEntity(...)  # required
)
```

- [LusidEntity](LusidEntity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

