# GeneralLedgerProfileMapping

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **mapping_filter** | **str** | Required | The filter syntax for the Mapping filter. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax |
| **levels** | **List[str]** | Required | References fields and properties on the associated Journal Entry Line and graph of associated objects. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GeneralLedgerProfileMapping import GeneralLedgerProfileMapping

instance = GeneralLedgerProfileMapping(
    mapping_filter="...",  # required — The filter syntax for the Mapping filter. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax
    levels=  # required — References fields and properties on the associated Journal Entry Line and graph of associated objects.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

