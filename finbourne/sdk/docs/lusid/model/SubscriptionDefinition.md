# SubscriptionDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | *No description available.* |
| **code** | **str** | Required | *No description available.* |
| **display_name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **timeline_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **address_keys** | **List[str]** | Optional | The set of addresses the subscriber wishes to receive. |
| **by_tax_lots** | **bool** | Optional | *No description available.* |
| **subscription_type** | **str** | Optional | The kind of data the subscription streams (holdings or transactions), defaulting to holdings.  Address keys and byTaxLots are not valid for a transactions subscription. Available values: Holdings, Transactions. |
| **start_effective_at** | **datetime** | Optional | *No description available.* |
| **end_effective_at** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SubscriptionDefinition import SubscriptionDefinition

instance = SubscriptionDefinition(
    scope="...",  # required
    code="...",  # required
    display_name="...",  # optional
    description="...",  # optional
    portfolio_id=ResourceId(...),  # required
    timeline_id=ResourceId(...),  # optional
    address_keys=,  # optional — The set of addresses the subscriber wishes to receive.
    by_tax_lots=True,  # optional
    subscription_type="...",  # optional — The kind of data the subscription streams (holdings or transactions), defaulting to holdings.  Address keys and byTaxLots are not valid for a transactions subscription. Available values: Holdings, Transactions.
    start_effective_at=datetime.now(),  # optional
    end_effective_at=datetime.now()  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

