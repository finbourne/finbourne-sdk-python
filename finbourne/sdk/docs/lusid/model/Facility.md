# Facility

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **facility_code** | **str** | Optional | The code of the Facility, unique within the Fund. |
| **display_name** | **str** | Required | The name of the Facility. |
| **description** | **str** | Optional | A description for the Facility. |
| **lender** | **str** | Required | The name of the lender providing the Facility. |
| **limit** | **float** | Required | The committed limit of the Facility. Must be greater than zero. |
| **currency** | **str** | Required | The three-letter currency code in which the Facility is denominated. |
| **rate_reference** | **str** | Optional | The reference rate the Facility interest is based on, for example SOFR. Optional. |
| **margin** | **float** | Required | The margin over the reference rate, expressed as a decimal. Must be zero or greater. |
| **commitment_fee_rate** | **float** | Required | The annual commitment fee rate charged on the undrawn balance, expressed as a decimal. Must be zero or greater. |
| **day_count_convention** | **str** | Required | The day count convention used to accrue interest. One of: Act360, Act365, Act365F, Thirty360. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Facility import Facility

instance = Facility(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    facility_code="...",  # optional — The code of the Facility, unique within the Fund.
    display_name="...",  # required — The name of the Facility.
    description="...",  # optional — A description for the Facility.
    lender="...",  # required — The name of the lender providing the Facility.
    limit=0.0,  # required — The committed limit of the Facility. Must be greater than zero.
    currency="...",  # required — The three-letter currency code in which the Facility is denominated.
    rate_reference="...",  # optional — The reference rate the Facility interest is based on, for example SOFR. Optional.
    margin=0.0,  # required — The margin over the reference rate, expressed as a decimal. Must be zero or greater.
    commitment_fee_rate=0.0,  # required — The annual commitment fee rate charged on the undrawn balance, expressed as a decimal. Must be zero or greater.
    day_count_convention="...",  # required — The day count convention used to accrue interest. One of: Act360, Act365, Act365F, Thirty360.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

