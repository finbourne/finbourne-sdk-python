# RolloverConstituent

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **contract_details** | [ContractDetails](ContractDetails.md) | Required | *No description available.* |
| **balance_change** | **float** | Required | Balance of the new contract holding. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RolloverConstituent import RolloverConstituent

instance = RolloverConstituent(
    contract_details=ContractDetails(...),  # required
    balance_change=0.0  # required — Balance of the new contract holding.
)
```


## Related Models

- [ContractDetails](ContractDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

