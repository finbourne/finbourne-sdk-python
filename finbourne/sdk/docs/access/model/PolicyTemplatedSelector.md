# PolicyTemplatedSelector

Templated selector for a policy template
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **application** | **str** | Required | The application that this selector definition applies to |
| **tag** | **str** | Required | The type of policy that this selector definition applies to |
| **selector** | [SelectorDefinition](SelectorDefinition.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.PolicyTemplatedSelector import PolicyTemplatedSelector

instance = PolicyTemplatedSelector(
    application="...",  # required — The application that this selector definition applies to
    tag="...",  # required — The type of policy that this selector definition applies to
    selector=SelectorDefinition(...)  # required
)
```

- [SelectorDefinition](SelectorDefinition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

