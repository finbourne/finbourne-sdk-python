# TransactionMatchingAlternativeId

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **property_key** | **str** | Required | An property key (from the &#39;Transaction&#39; domain) that can be used as an alternative to TransactionId when matching transactions to settlement instructions. This property must be pre-defined and must be present on the transaction in order to be used for matching. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionMatchingAlternativeId import TransactionMatchingAlternativeId

instance = TransactionMatchingAlternativeId(
    property_key="..."  # required — An property key (from the &#39;Transaction&#39; domain) that can be used as an alternative to TransactionId when matching transactions to settlement instructions. This property must be pre-defined and must be present on the transaction in order to be used for matching.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

