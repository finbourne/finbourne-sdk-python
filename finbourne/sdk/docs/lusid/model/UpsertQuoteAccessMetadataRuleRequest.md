# UpsertQuoteAccessMetadataRuleRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [QuoteAccessMetadataRuleId](QuoteAccessMetadataRuleId.md) | Required | *No description available.* |
| **metadata** | **Dict[str, Optional[List[AccessMetadataValue]]]** | Required | The access control metadata to assign to quotes that match the identifier |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertQuoteAccessMetadataRuleRequest import UpsertQuoteAccessMetadataRuleRequest

instance = UpsertQuoteAccessMetadataRuleRequest(
    id=QuoteAccessMetadataRuleId(...),  # required
    metadata=  # required — The access control metadata to assign to quotes that match the identifier
)
```


## Related Models

- [QuoteAccessMetadataRuleId](QuoteAccessMetadataRuleId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

