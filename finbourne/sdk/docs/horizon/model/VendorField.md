# VendorField

Reference to a specific vendor field
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **package** | **str** | Required | The vendor package it is included in |
| **var_field** | **str** | Required | The name of the field |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.VendorField import VendorField

instance = VendorField(
    package="...",  # required — The vendor package it is included in
    var_field="..."  # required — The name of the field
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

