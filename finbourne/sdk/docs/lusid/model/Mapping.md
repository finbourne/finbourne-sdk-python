# Mapping

Defines the rule set to be used to determine if entries should be considered as a match.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope for this mapping. |
| **code** | **str** | Required | The code for this mapping. |
| **name** | **str** | Required | The mapping name |
| **reconciliation_type** | **str** | Required | What type of reconciliation this mapping is for |
| **rules** | [List[MappingRule]](MappingRule.md) | Optional | The rules in this mapping, keyed by the left field/property name |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Mapping import Mapping

instance = Mapping(
    scope="...",  # required — The scope for this mapping.
    code="...",  # required — The code for this mapping.
    name="...",  # required — The mapping name
    reconciliation_type="...",  # required — What type of reconciliation this mapping is for
    rules=[]  # optional — The rules in this mapping, keyed by the left field/property name
)
```

- [MappingRule](MappingRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

