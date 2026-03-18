# CdsProtectionDetailSpecification

CDSs generally conform to fairly standard definitions, but can be tweaked in a number of different ways.  This class gathers a number of common features which may deviate. These will default to the market standard when  no overrides are provided.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **seniority** | **str** | Optional | The seniority level of the CDS.  Supported string (enumeration) values are: [SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2].  Defaults to \&quot;SUB\&quot; if not set. Default: `'SUB'` |
| **restructuring_type** | **str** | Optional | The restructuring clause.  Supported string (enumeration) values are: [CR, MR, MM, XR]. Defaults to \&quot;MM\&quot; if not set. Default: `'MM'` |
| **protect_start_day** | **bool** | Optional | Does the protection leg pay out in the case of default on the start date. Defaults to true if not set. Default: `True` |
| **pay_accrued_interest_on_default** | **bool** | Optional | Should accrued interest on the premium leg be paid if a credit event occurs. Defaults to true if not set. Default: `True` |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CdsProtectionDetailSpecification import CdsProtectionDetailSpecification

instance = CdsProtectionDetailSpecification(
    seniority="...",  # optional — The seniority level of the CDS.  Supported string (enumeration) values are: [SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2].  Defaults to \&quot;SUB\&quot; if not set.
    restructuring_type="...",  # optional — The restructuring clause.  Supported string (enumeration) values are: [CR, MR, MM, XR]. Defaults to \&quot;MM\&quot; if not set.
    protect_start_day=True,  # optional — Does the protection leg pay out in the case of default on the start date. Defaults to true if not set.
    pay_accrued_interest_on_default=True  # optional — Should accrued interest on the premium leg be paid if a credit event occurs. Defaults to true if not set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

