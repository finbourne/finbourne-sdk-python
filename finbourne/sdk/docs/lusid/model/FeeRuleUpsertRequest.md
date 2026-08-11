# FeeRuleUpsertRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional |  |
| **transaction_property_key** | **str** | Required |  |
| **transaction_type** | **str** | Required |  |
| **country** | **str** | Required |  |
| **counterparty** | **str** | Required |  |
| **transaction_currency** | **str** | Required |  |
| **settlement_currency** | **str** | Required |  |
| **execution_broker** | **str** | Required |  |
| **custodian** | **str** | Required |  |
| **exchange** | **str** | Required |  |
| **fee** | [CalculationInfo](CalculationInfo.md) | Required | *No description available.* |
| **min_fee** | [CalculationInfo](CalculationInfo.md) | Optional | *No description available.* |
| **max_fee** | [CalculationInfo](CalculationInfo.md) | Optional | *No description available.* |
| **additional_keys** | **Dict[str, Optional[str]]** | Optional |  |
| **description** | **str** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FeeRuleUpsertRequest import FeeRuleUpsertRequest

instance = FeeRuleUpsertRequest(
    code="...",  # optional — 
    transaction_property_key="...",  # required — 
    transaction_type="...",  # required — 
    country="...",  # required — 
    counterparty="...",  # required — 
    transaction_currency="...",  # required — 
    settlement_currency="...",  # required — 
    execution_broker="...",  # required — 
    custodian="...",  # required — 
    exchange="...",  # required — 
    fee=CalculationInfo(...),  # required
    min_fee=CalculationInfo(...),  # optional
    max_fee=CalculationInfo(...),  # optional
    additional_keys=,  # optional — 
    description="..."  # optional — 
)
```

- [CalculationInfo](CalculationInfo.md)
- [CalculationInfo](CalculationInfo.md)
- [CalculationInfo](CalculationInfo.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

