# PolicyTemplateUpdateRequest

Update policy template request
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The display name of the policy template being created |
| **description** | **str** | Required | Description of the policy template being craeted |
| **templated_selectors** | [List[PolicyTemplatedSelector]](PolicyTemplatedSelector.md) | Required | The selector definitions of policies included in this policy template |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.PolicyTemplateUpdateRequest import PolicyTemplateUpdateRequest

instance = PolicyTemplateUpdateRequest(
    display_name="...",  # required — The display name of the policy template being created
    description="...",  # required — Description of the policy template being craeted
    templated_selectors=[]  # required — The selector definitions of policies included in this policy template
)
```

- [PolicyTemplatedSelector](PolicyTemplatedSelector.md) — used in `templated_selectors`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

