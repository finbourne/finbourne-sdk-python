# ValueConstraints

Constraints that should be applied to a Tasks fields
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **constraint_type** | **str** | Required | Whether the constraint is a suggestion or should be enforced via validation (e.g. Suggested, Validated) |
| **value_source_type** | **str** | Required | The source of the acceptable values (e.g. AcceptableValues) |
| **acceptable_values** | **List[object]** | Required | The acceptable values for the field |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ValueConstraints import ValueConstraints

instance = ValueConstraints(
    constraint_type="...",  # required — Whether the constraint is a suggestion or should be enforced via validation (e.g. Suggested, Validated)
    value_source_type="...",  # required — The source of the acceptable values (e.g. AcceptableValues)
    acceptable_values=  # required — The acceptable values for the field
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

