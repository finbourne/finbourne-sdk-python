# FxConventions

The conventions for the calculation of FX fixings, where the fixing rate is expected to be the amount of  DomCcy per unit of FgnCcy.  As an example, assume the required fixing is the WM/R 4pm mid closing rate for the USD amount per 1 EUR.  This is published with RIC EURUSDFIXM=WM, which would be the FixingReference, with FgnCcy EUR and DomCcy USD.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fgn_ccy** | **str** | Required | The foreign currency |
| **dom_ccy** | **str** | Required | The domestic currency |
| **fixing_reference** | **str** | Required | The reference name used to find the desired quote |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxConventions import FxConventions

instance = FxConventions(
    fgn_ccy="...",  # required — The foreign currency
    dom_ccy="...",  # required — The domestic currency
    fixing_reference="..."  # required — The reference name used to find the desired quote
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

