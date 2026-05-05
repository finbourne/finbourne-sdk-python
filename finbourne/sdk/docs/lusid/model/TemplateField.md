# TemplateField

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | *No description available.* |
| **specificity** | **str** | Required | Available values: AllEventsAndHoldings, InstrumentEventType, ElectionType. |
| **description** | **str** | Required | *No description available.* |
| **type** | **str** | Required | Available values: String, Decimal, InstrumentScope, Currency, DateTime, PriceType, InstrumentId, PropertyKey, Boolean. |
| **availability** | **str** | Required | Available values: Guaranteed, DataDependent, Informational. |
| **usage** | **List[str]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TemplateField import TemplateField

instance = TemplateField(
    field_name="...",  # required
    specificity="...",  # required — Available values: AllEventsAndHoldings, InstrumentEventType, ElectionType.
    description="...",  # required
    type="...",  # required — Available values: String, Decimal, InstrumentScope, Currency, DateTime, PriceType, InstrumentId, PropertyKey, Boolean.
    availability="...",  # required — Available values: Guaranteed, DataDependent, Informational.
    usage=  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

