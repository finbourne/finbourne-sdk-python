# PolicyTemplateResponse

Response object for a policy template
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Optional | Display name of the policy template being created |
| **scope** | **str** | Optional | The Scope of the policy template being created |
| **code** | **str** | Optional | The Code of the policy template being created |
| **description** | **str** | Optional | Description of the policy template being created |
| **applications** | **List[str]** | Optional | List of applications that this policy template covers |
| **tags** | **List[str]** | Optional | List of policy types that this policy template covers |
| **templated_selectors** | [List[PolicyTemplatedSelector]](PolicyTemplatedSelector.md) | Optional | The selector definitions of policies included in this policy template |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.PolicyTemplateResponse import PolicyTemplateResponse

instance = PolicyTemplateResponse(
    display_name="...",  # optional — Display name of the policy template being created
    scope="...",  # optional — The Scope of the policy template being created
    code="...",  # optional — The Code of the policy template being created
    description="...",  # optional — Description of the policy template being created
    applications=,  # optional — List of applications that this policy template covers
    tags=,  # optional — List of policy types that this policy template covers
    templated_selectors=[]  # optional — The selector definitions of policies included in this policy template
)
```

- [PolicyTemplatedSelector](PolicyTemplatedSelector.md) — used in `templated_selectors`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

