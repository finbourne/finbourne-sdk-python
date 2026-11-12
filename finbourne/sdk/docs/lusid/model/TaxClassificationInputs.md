# TaxClassificationInputs

The instrument static the decision tree reads. A missing flag is a missing input, not a false.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **loan_relationship_asset** | **bool** | Optional | Whether the instrument is a loan relationship asset. |
| **index_linked_gilt** | **bool** | Optional | Whether the instrument is an index-linked gilt. |
| **chargeable_asset** | **bool** | Optional | Whether disposals of the instrument give rise to chargeable gains. |
| **cis_non_transparent** | **bool** | Optional | Whether the instrument is a non-transparent collective investment scheme. |
| **cis_transparent** | **bool** | Optional | Whether the instrument is a transparent collective investment scheme. |
| **derivative** | **bool** | Optional | Whether the instrument is a derivative contract. |
| **derivative_financial_future** | **bool** | Optional | Whether the derivative is a financial future or option within the chargeable gains rules. |
| **derivative_pooled_security** | **bool** | Optional | Whether the derivative is pooled as a security. |
| **private_equity** | **bool** | Optional | Whether the instrument is a private equity holding. |
| **real_estate** | **bool** | Optional | Whether the instrument is a real estate holding. |
| **qualifying_investments_percent** | **float** | Optional | The percentage of the scheme&#39;s assets that are qualifying (non-equity) investments; more than 60 percent makes the scheme a bond fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxClassificationInputs import TaxClassificationInputs

instance = TaxClassificationInputs(
    loan_relationship_asset=True,  # optional — Whether the instrument is a loan relationship asset.
    index_linked_gilt=True,  # optional — Whether the instrument is an index-linked gilt.
    chargeable_asset=True,  # optional — Whether disposals of the instrument give rise to chargeable gains.
    cis_non_transparent=True,  # optional — Whether the instrument is a non-transparent collective investment scheme.
    cis_transparent=True,  # optional — Whether the instrument is a transparent collective investment scheme.
    derivative=True,  # optional — Whether the instrument is a derivative contract.
    derivative_financial_future=True,  # optional — Whether the derivative is a financial future or option within the chargeable gains rules.
    derivative_pooled_security=True,  # optional — Whether the derivative is pooled as a security.
    private_equity=True,  # optional — Whether the instrument is a private equity holding.
    real_estate=True,  # optional — Whether the instrument is a real estate holding.
    qualifying_investments_percent=0.0  # optional — The percentage of the scheme&#39;s assets that are qualifying (non-equity) investments; more than 60 percent makes the scheme a bond fund.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

