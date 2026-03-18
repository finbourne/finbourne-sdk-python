# OnboardInstrumentRequest

The full structure of a instrument creation / onboarding request
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **data_results** | [List[OpenFigiPermIdResult]](OpenFigiPermIdResult.md) | Required | Enumerable packed OpenFigi/PermId information used to create instruments |
| **primary_vendor_key** | **str** | Optional | Primary vendor used to master instrument from Unknown to an asset type |
| **secondary_vendor_keys** | **List[str]** | Optional | Secondary vendors used to decorate additional properties |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.OnboardInstrumentRequest import OnboardInstrumentRequest

instance = OnboardInstrumentRequest(
    data_results=[],  # required — Enumerable packed OpenFigi/PermId information used to create instruments
    primary_vendor_key="...",  # optional — Primary vendor used to master instrument from Unknown to an asset type
    secondary_vendor_keys=  # optional — Secondary vendors used to decorate additional properties
)
```


## Related Models

- [OpenFigiPermIdResult](OpenFigiPermIdResult.md) — used in `data_results`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

