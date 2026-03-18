# CreditRating

Object describing a credit rating,  which assesses the stability and credit worthiness of a legal entity  and hence its likelihood of defaulting on its outstanding obligations (typically debt).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rating_source** | **str** | Required | The provider of the credit rating, which will typically be an agency such as Moody&#39;s or Standard and Poor. |
| **rating** | **str** | Required | The credit rating provided by the rating source. This would expected to be consistent with the rating scheme of that agency/source. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreditRating import CreditRating

instance = CreditRating(
    rating_source="...",  # required — The provider of the credit rating, which will typically be an agency such as Moody&#39;s or Standard and Poor.
    rating="..."  # required — The credit rating provided by the rating source. This would expected to be consistent with the rating scheme of that agency/source.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

