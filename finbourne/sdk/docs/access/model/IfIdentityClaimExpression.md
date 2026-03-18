# IfIdentityClaimExpression

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **claim_type** | **str** | Required | *No description available.* |
| **claim_value_type** | **str** | Optional | *No description available.* |
| **claim_issuer** | **str** | Optional | *No description available.* |
| **claim_original_issuer** | **str** | Optional | *No description available.* |
| **operator** | [TextOperator](TextOperator.md) | Required | *No description available.* |
| **value** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.IfIdentityClaimExpression import IfIdentityClaimExpression

instance = IfIdentityClaimExpression(
    claim_type="...",  # required
    claim_value_type="...",  # optional
    claim_issuer="...",  # optional
    claim_original_issuer="...",  # optional
    operator=TextOperator(...),  # required
    value="..."  # optional
)
```

- [TextOperator](TextOperator.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

