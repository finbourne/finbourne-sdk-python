# DescribedAddressKey

An address key with additional data describing what this key is for.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **address_key** | **str** | Optional | Address key of some underlying object e.g. Valuation/PV, Instrument/Features |
| **description** | **str** | Optional | Description of the address key. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DescribedAddressKey import DescribedAddressKey

instance = DescribedAddressKey(
    address_key="...",  # optional — Address key of some underlying object e.g. Valuation/PV, Instrument/Features
    description="..."  # optional — Description of the address key.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

