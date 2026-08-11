# IfExpression

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **if_request_header_expression** | [IfRequestHeaderExpression](IfRequestHeaderExpression.md) | Optional | *No description available.* |
| **if_identity_claim_expression** | [IfIdentityClaimExpression](IfIdentityClaimExpression.md) | Optional | *No description available.* |
| **if_identity_scope_expression** | [IfIdentityScopeExpression](IfIdentityScopeExpression.md) | Optional | *No description available.* |
| **if_via_api_expression** | [IfViaApiExpression](IfViaApiExpression.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.IfExpression import IfExpression

instance = IfExpression(
    if_request_header_expression=IfRequestHeaderExpression(...),  # optional
    if_identity_claim_expression=IfIdentityClaimExpression(...),  # optional
    if_identity_scope_expression=IfIdentityScopeExpression(...),  # optional
    if_via_api_expression=IfViaApiExpression(...)  # optional
)
```


## Related Models

- [IfRequestHeaderExpression](IfRequestHeaderExpression.md)
- [IfIdentityClaimExpression](IfIdentityClaimExpression.md)
- [IfIdentityScopeExpression](IfIdentityScopeExpression.md)
- [IfViaApiExpression](IfViaApiExpression.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

