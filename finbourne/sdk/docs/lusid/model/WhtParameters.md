# WhtParameters

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **wht_config** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **tax_country** | **str** | Required | The holder&#39;s country of tax residence, matched against the taxCountry field of the rate datasets. |
| **profile_type** | **str** | Required | The holder&#39;s tax profile, matched against the profileType field of the rate datasets. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WhtParameters import WhtParameters

instance = WhtParameters(
    wht_config=ResourceId(...),  # required
    tax_country="...",  # required — The holder&#39;s country of tax residence, matched against the taxCountry field of the rate datasets.
    profile_type="..."  # required — The holder&#39;s tax profile, matched against the profileType field of the rate datasets.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

