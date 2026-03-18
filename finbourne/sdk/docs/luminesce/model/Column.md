# Column

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **is_primary_key** | **bool** | Optional | *No description available.* |
| **is_main** | **bool** | Optional | *No description available.* |
| **is_required_by_provider** | **bool** | Optional | *No description available.* |
| **mandatory_for_actions** | **str** | Optional | *No description available.* |
| **lineage** | [Lineage](Lineage.md) | Optional | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **type** | [DataType](DataType.md) | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **display_name** | **str** | Optional | *No description available.* |
| **condition_usage** | [ConditionAttributes](ConditionAttributes.md) | Optional | *No description available.* |
| **sample_values** | **str** | Optional | *No description available.* |
| **allowed_values** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.Column import Column

instance = Column(
    is_primary_key=True,  # optional
    is_main=True,  # optional
    is_required_by_provider=True,  # optional
    mandatory_for_actions="...",  # optional
    lineage=Lineage(...),  # optional
    name="...",  # optional
    type=DataType(...),  # optional
    description="...",  # optional
    display_name="...",  # optional
    condition_usage=ConditionAttributes(...),  # optional
    sample_values="...",  # optional
    allowed_values="..."  # optional
)
```

- [Lineage](Lineage.md)
- [DataType](DataType.md)
- [ConditionAttributes](ConditionAttributes.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

